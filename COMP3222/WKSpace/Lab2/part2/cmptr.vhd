LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY cmptr IS
	PORT (V				: IN	STD_LOGIC_VECTOR(3 DOWNTO 0);
			Z				: OUT	STD_LOGIC);
END cmptr;

ARCHITECTURE Behavior OF cmptr IS

BEGIN
	Z <= V(3) AND (V(2) OR V(1));
END Behavior;