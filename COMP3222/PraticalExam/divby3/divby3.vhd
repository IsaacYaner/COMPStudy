library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;


entity divby3 is
    Port (	clk 		: in  STD_LOGIC;     -- use manual clock
			Resetn 		: in  STD_LOGIC;
			A			: in  STD_LOGIC_VECTOR(7 downto 0);
			s			: in  STD_LOGIC;
			R			: out STD_LOGIC_VECTOR(7 downto 0);
			Div3		: out STD_LOGIC;
			Done		: out STD_LOGIC);
end divby3;

architecture behavioural of divby3 is
	type STATE_TYPE is (SI, S1, S3, S4);
	signal y, y_next: STATE_TYPE;
	signal calcsub, LD : STD_LOGIC;
	SIGNAL sub : STD_LOGIC_VECTOR(7 DOWNTO 0);
	
begin
	
  -- FSM transitions
	statetable : PROCESS(y, Resetn, s, sub)
	BEGIN
		IF Resetn = '0' THEN
			y_next <= SI;
		ELSE 
			CASE y IS
				WHEN SI =>
					IF s = '1' THEN
						y_next <= S1;
					ELSE
						y_next <= SI;
					END IF;
				WHEN S1 =>
					IF (sub < 3)THEN
						IF sub = 0 THEN
							y_next <= S3;
						ELSE
							y_next <= S4;
						END IF;
					ELSE
						y_next <= S1;
					END IF;
				WHEN S3 =>
					IF s = '1' THEN
						y_next <= S3;
					ELSE
						y_next <= SI;
					END IF;
				WHEN S4 =>
					IF s = '1' THEN
						y_next <= S4;
					ELSE
						y_next <= SI;
					END IF;
			END CASE;
		END IF;
	END PROCESS;
	
	fsmflipflops : PROCESS(y_next, Resetn, clk)
	BEGIN
		IF Resetn = '0' THEN
			y <= SI;
		ELSIF clk'event AND clk = '1' THEN
			y <= y_next;
		END IF;
	END PROCESS;
	
  -- FSM outputs
	fsmoutputs : PROCESS(y, s, sub)
	BEGIN
		calcsub <= '0'; LD <= '0'; div3 <= '0'; Done <= '0';
		CASE y IS
			WHEN SI =>
				IF s = '0' THEN
					LD <= '1';
				END IF;
			WHEN S1 =>
				IF (sub < 3)THEN
					IF sub = 0 THEN
						div3 <= '1';
						Done <= '1';
					ELSE
						Done <= '1';
					END IF;
				ELSE
					calcsub <= '1';
				END IF;
			WHEN S3 =>
				div3 <= '1';
				Done <= '1';
			WHEN S4 =>
				Done <= '1';
		END CASE;
	END PROCESS;
  -- Datapath components
	
	R <= sub;
	
	submanipulating : PROCESS(clk, calcsub, Resetn)
	BEGIN
		IF Resetn = '0' THEN
			sub <= (others => '0');
		ELSIF clk'event AND clk = '1' THEN
			IF LD = '1' THEN
				sub <= A;
			ELSIF calcsub = '1' THEN
				sub <= sub - 3;
			END IF;
		END IF;
	END PROCESS;
	
end behavioural;