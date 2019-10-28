LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY counter16bit IS
	PORT (Enable, Cloc, Clear	: IN	STD_LOGIC;
			Cout						: OUT STD_LOGIC_VECTOR(15 DOWNTO 0));
END counter16bit;

ARCHITECTURE Behavior of counter16bit IS

SIGNAL Q : STD_LOGIC_VECTOR(15 DOWNTO 0);

BEGIN
	PROCESS(Clear, Cloc, Enable)
	BEGIN
		IF Clear = '1' THEN												--Hi voltage asyn reset.
			Q <= (others => '0');
		ELSIF Cloc'event AND Cloc = '1' THEN
		    IF Enable = '1' THEN										--Counter.
			    Q <= Q+1;
		    END IF;
		END IF;
	END PROCESS;
	Cout <= Q;																--Connect to output.
END Behavior;

--One LUT and one 16 bit adder--

--1s/7 nano secondes