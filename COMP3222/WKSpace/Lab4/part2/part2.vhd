LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY part2 IS
	PORT (Enable, Cloc, Clear	: IN	STD_LOGIC;
			Cout						: OUT STD_LOGIC_VECTOR(15 DOWNTO 0));
END part2;

ARCHITECTURE Behavior of part2 IS

SIGNAL Q : STD_LOGIC_VECTOR(15 DOWNTO 0);

BEGIN
	PROCESS(Clear, Cloc, Enable)
	BEGIN
		IF Clear = '1' THEN
			Q <= (others => '0');
		ELSIF Cloc'event AND Cloc = '1' AND Enable = '1' THEN
			Q <= Q+1;
		END IF;
	END PROCESS;
	Cout <= Q;
END Behavior;

--One LUT and one 16 bit adder--

--1s/7 nano secondes