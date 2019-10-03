LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY numb IS
	PORT (N0					:	OUT	STD_LOGIC_VECTOR(6 DOWNTO 0);
			Cin				:	IN		STD_LOGIC_VECTOR(3 DOWNTO 0));
END numb;

ARCHITECTURE Behavior OF numb IS

BEGIN
	N0(0)<=(NOT(Cin(3)) AND NOT(Cin(2)) AND NOT(Cin(1)) AND Cin(0)) OR (NOT(Cin(3)) AND Cin(2) AND NOT(Cin(1)) AND NOT(Cin(0)));
	N0(1)<=(NOT(Cin(3)) AND Cin(2) AND NOT(Cin(1)) AND Cin(0)) OR (NOT(Cin(3)) AND Cin(2) AND Cin(1) AND NOT(Cin(0)));
	N0(2)<=(NOT(Cin(3)) AND NOT(Cin(2)) AND Cin(1) AND NOT(Cin(0)));
	N0(3)<=(NOT(Cin(3)) AND NOT(Cin(2)) AND NOT(Cin(1)) AND Cin(0)) OR (NOT(Cin(3)) AND Cin(2) AND NOT(Cin(1)) AND NOT(Cin(0))) OR (NOT(Cin(3)) AND Cin(2) AND Cin(1) AND Cin(0));
	N0(4)<=(NOT(Cin(3)) AND Cin(0)) OR (NOT(Cin(3)) AND Cin(2) AND NOT(Cin(1)) AND NOT(Cin(0))) OR (NOT(Cin(2)) AND NOT(Cin(1)) AND Cin(0));
	N0(5)<=(NOT(Cin(3)) AND NOT(Cin(2)) AND Cin(0)) OR (NOT(Cin(3)) AND NOT(Cin(2)) AND Cin(1)) OR (NOT(Cin(3)) AND Cin(1) AND Cin(0));
	N0(6)<=(NOT(Cin(3)) AND NOT(Cin(2)) AND NOT(Cin(1))) OR (NOT(Cin(3)) AND Cin(2) AND Cin(1) AND Cin(0));
END Behavior;