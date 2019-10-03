LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY CirC IS
	PORT (V				: IN	STD_LOGIC_VECTOR(3 DOWNTO 0);
			M				: OUT	STD_LOGIC_VECTOR(3 DOWNTO 0));
END CirC;

ARCHITECTURE Behavior OF CirC IS

BEGIN
	M(0) <= V(0);
	M(1) <= NOT(V(1));
	M(2) <= NOT(V(1));
	M(3) <= V(1);
END Behavior;