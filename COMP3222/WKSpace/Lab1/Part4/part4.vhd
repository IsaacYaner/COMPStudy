LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY part4 IS
	PORT (SW	: IN	STD_LOGIC_VECTOR(1 DOWNTO 0);
			HEX0	: OUT	STD_LOGIC_VECTOR(0 TO 6));--Why is here TO instead of DOWNTO?
END part4;

ARCHITECTURE Behavior OF part4 IS 

BEGIN
	HEX0(0)<=not(not(SW(1)) and SW(0));--Is the bracket necessary?
	HEX0(1)<=(SW(0));
	HEX0(2)<=(SW(0));
	HEX0(3)<=(SW(1));
	HEX0(4)<=(SW(1));
	HEX0(5)<=not(not(SW(1)) and SW(0));
	HEX0(6)<=(SW(1));
END Behavior;