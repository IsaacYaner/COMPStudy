library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;



	type STATE_TYPE is (SI, S1, S2, S3);
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
					
				WHEN S1 =>
					
				WHEN S2 =>
					
				WHEN S3 =>
					
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
				
			WHEN S1 =>
				
			WHEN S2 =>
				
			WHEN S3 =>
				
		END CASE;
	END PROCESS;
   -- Datapath components
	
	-- Wire out R <= sub;
	
	submanipulating : PROCESS(clk, calcsub, Resetn)
	BEGIN
		IF Resetn = '0' THEN
			
		ELSIF clk'event AND clk = '1' THEN
			
		END IF;
	END PROCESS;
	
end behavioural;