LIBRARY IEEE;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY CounterFSM IS
	GENERIC(N : NATURAL := 8); -- How to use generic map?
	PORT (Cin	 : IN	 STD_LOGIC_VECTOR(N-1 DOWNTO 0);
			s		 : IN	 STD_LOGIC;
			Resetn : IN	 STD_LOGIC;
			CLK	 : IN  STD_LOGIC;
			Cout	 : OUT STD_LOGIC_VECTOR(N-1 DOWNTO 0);
			Done	 : OUT STD_LOGIC);
END CounterFSM;

ARCHITECTURE Behavior OF CounterFSM IS

TYPE State_type IS (S1, S2, S3);
SIGNAL state, nextState : State_type;
SIGNAL LA, incRes, resRes, Rshift, markDone : STD_LOGIC;
SIGNAL A, result : STD_LOGIC_VECTOR(N-1 DOWNTO 0);

BEGIN 
	
	Cout <= result;
	
	datas: PROCESS(Resetn, CLK, LA, incRes, resRes, Rshift, markDone)
	BEGIN 
		IF Resetn = '0' THEN
			A <= (others => '0');
			result <= (others => '0');
			Done <= '0';
		ELSIF CLK'event AND CLK = '1' THEN
			IF LA = '1' THEN
				A <= Cin;
			END IF;
			IF incRes = '1' THEN
				result <= result + 1;
			END IF;
			IF resRes = '1' THEN 
				result <= (others => '0');
			END IF;
			IF Rshift = '1' THEN
				A(N-2 DOWNTO 0) <= A(N-1 DOWNTO 1);
				A(N-1) <= '0';
			END IF;
			IF markDone = '1' THEN
				Done <= '1';
			ELSE
				Done <= '0';
			END IF;
		END IF;
	END PROCESS;
	-- load a   --
	-- result   --
	-- reset    --
	-- shiftA   --
	-- MarkDone --

	statetable: PROCESS(Resetn, state, s, A)
	BEGIN 
		IF Resetn = '1' THEN
			CASE state IS
				WHEN S1 =>
					IF s = '1' THEN 
						nextState <= S2;
					ELSE 
						nextState <= S1;
					END IF;
				WHEN S2 => 
					IF A = "00000000" THEN
						nextState <= S3;
					ELSE 
						nextState <= S2;
					END IF;
				WHEN S3 =>
					IF s = '0' THEN
						nextState <= S1;
					ELSE 
						nextState <= S3;
					END IF;
			END CASE;
		ELSE nextState <= S1;
		END IF;
			
	END PROCESS;

	controlsignals: PROCESS(Resetn, state, A)
	BEGIN 
		LA <= '0';
		incRes <= '0';
		resRes <= '0';
		Rshift <= '0';
		markDone <= '0';
		IF Resetn = '1' THEN
			CASE state IS
				WHEN S1 =>
					LA <= '1';
					resRes <= '1';
				WHEN S2 =>
					IF A(0) = '1' THEN 
						incRes <= '1';
					END IF;
					Rshift <= '1';
				WHEN S3 =>
					markDone <= '1';
			END CASE;
		END IF;
	END PROCESS;
	
	fsmflipflops: PROCESS(CLK, Resetn)
	BEGIN
		IF Resetn = '0' THEN
			state <= S1;
		ELSIF CLK'event AND CLK = '1' THEN 
			state <= nextState;
		END IF;
	END PROCESS;
	
END Behavior;