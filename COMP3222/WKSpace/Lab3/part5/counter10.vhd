LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY counter10 IS
	PORT (Enable, Cloc, Clear	: IN	STD_LOGIC;
			Cout						: OUT STD_LOGIC_VECTOR(3 DOWNTO 0));
END counter10;

ARCHITECTURE Behavior of counter10 IS

SIGNAL Q : STD_LOGIC_VECTOR(3 DOWNTO 0);

BEGIN

	PROCESS(Clear, Cloc, Enable)
	BEGIN
		IF Clear = '1' THEN
			Q <= (others => '0');
		
		ELSIF Cloc'event AND Cloc = '1' THEN
			IF Enable = '1' THEN
			
				IF(Q = 9) THEN
					Q <= (others => '0');
				ELSE 
					Q <= Q+1;
				END IF;
			
			END IF;
		END IF;
	END PROCESS;
	Cout <= Q;
END Behavior;

--One LUT and one 16 bit adder--

--1s/7 nano secondes