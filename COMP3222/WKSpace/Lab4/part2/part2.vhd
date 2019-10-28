LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY part2 IS
	PORT (Enable, Cloc, Clear	: IN	STD_LOGIC;
			Cout						: OUT STD_LOGIC_VECTOR(15 DOWNTO 0));
END part2;

ARCHITECTURE Behavior of part2 IS

COMPONENT counter16bit IS
	PORT (Enable, Cloc, Clear	: IN	STD_LOGIC;
			Cout						: OUT STD_LOGIC_VECTOR(15 DOWNTO 0));
END COMPONENT;

BEGIN

	countingUp : counter16bit PORT MAP (Enable, Cloc, Clear, Cout);

END Behavior;

--One LUT and one 16 bit adder--

--1s/7 nano secondes