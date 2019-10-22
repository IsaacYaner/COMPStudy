LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY MHZ5 IS
	PORT (CLK	: IN	STD_LOGIC;
			Cout	: OUT	STD_LOGIC_VECTOR(3 DOWNTO 0));
END MHZ5;

ARCHITECTURE Behavior OF MHZ5 IS

SIGNAL Enable : STD_LOGIC;
SIGNAL Q : STD_LOGIC_VECTOR(3 DOWNTO 0);
SIGNAL RESV : STD_LOGIC_VECTOR(25 DOWNTO 0);

BEGIN
	PROCESS(CLK)
	BEGIN
			
		IF CLK'event AND CLK = '1' THEN
			RESV <= RESV + 1;
			IF RESV = 50000000 THEN
				RESV <= (others => '0');
				Enable <= '1';
			ELSE
				Enable <= '0';
			END IF;
		END IF;
	END PROCESS;
	
	PROCESS(CLK, Enable)
	BEGIN
	
			IF CLK'EVENT AND CLK = '1' THEN
			   IF Enable = '1' THEN
					IF Q = 9 THEN 		--Reset
						Q <= (others => '0');
					ELSE
						Q <= Q+1;
					END IF;
				END IF;
			END IF;
	END PROCESS;
	Cout <= Q;
END Behavior;