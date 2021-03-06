LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY CirA IS
	PORT (V				: IN	STD_LOGIC_VECTOR(2 DOWNTO 0);
			M				: OUT	STD_LOGIC_VECTOR(2 DOWNTO 0));
END CirA;

ARCHITECTURE Behavior OF CirA IS

BEGIN
	M(0) <= (V(1) AND V(0)) OR (V(2) AND V(0));
	M(1) <= V(2) AND NOT(V(1));
	M(2) <= V(2) AND V(1);
END Behavior;