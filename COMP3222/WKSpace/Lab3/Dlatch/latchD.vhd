-- A gated RS latch desribed the hard way
LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY latchD IS
	PORT (SW		: IN	STD_LOGIC_VECTOR(1 DOWNTO 0);
			LEDR	: OUT	STD_LOGIC_VECTOR(0 DOWNTO 0));
END latchD;

ARCHITECTURE Structural OF latchD IS

COMPONENT part2 IS
	PORT (Clk, D : IN STD_LOGIC;
			Q : OUT STD_LOGIC);
END COMPONENT;

BEGIN
	DoDlatch : part2 PORT MAP (SW(1), SW(0), LEDR(0));
END Structural;