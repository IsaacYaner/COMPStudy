-- A gated RS latch desribed the hard way
LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY part2 IS
	PORT (Clk, D : IN STD_LOGIC;
			Q : OUT STD_LOGIC);
END part2;

ARCHITECTURE Structural OF part2 IS

SIGNAL R_g, S_g, Qa, Qb : STD_LOGIC ;
ATTRIBUTE keep : boolean;
ATTRIBUTE keep of R_g, S_g, Qa, Qb : SIGNAL IS true;

BEGIN
	R_g <= NOT(NOT(D) AND Clk);
	S_g <= NOT(D AND Clk);
	Qa <= NOT (S_g AND Qb);
	Qb <= NOT (R_g AND Qa);
	Q <= Qa;
END Structural;