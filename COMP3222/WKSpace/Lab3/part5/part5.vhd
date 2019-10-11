LIBRARY IEEE;
USE ieee.std_logic_1164.all;

ENTITY part5 IS
	PORT (SW		: IN	STD_LOGIC_VECTOR(7 DOWNTO 0);
			KEY	: IN	STD_LOGIC_VECTOR(1 DOWNTO 0);
			HEX0, HEX1, HEX2, HEX3	: OUT	STD_LOGIC_VECTOR(6 DOWNTO 0));
END part5;

ARCHITECTURE Behavior OF part5 IS

COMPONENT BCD8bit IS
	PORT (SW		: IN	STD_LOGIC_VECTOR(7 DOWNTO 0);
			KEY	: IN	STD_LOGIC_VECTOR(1 DOWNTO 0);
			HEX0, HEX1, HEX2, HEX3	: OUT	STD_LOGIC_VECTOR(6 DOWNTO 0));
END COMPONENT;

BEGIN
	StartD : BCD8bit PORT MAP (SW, KEY, HEX0, HEX1, HEX2, HEX3);
END Behavior;