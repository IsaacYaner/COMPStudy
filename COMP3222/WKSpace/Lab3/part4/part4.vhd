LIBRARY ieee ;
USE ieee.std_logic_1164.all;

ENTITY part4 IS
	PORT (Clk, D		: IN	STD_LOGIC;
			Qa, Qb, Qc	: OUT	STD_LOGIC);
END part4;

ARCHITECTURE Behavior OF part4 IS

COMPONENT Dflop IS
	PORT (Clk, D	: IN	STD_LOGIC;
			Q			: OUT	STD_LOGIC);
END COMPONENT;

COMPONENT Nflop IS
	PORT (Clk, D	: IN	STD_LOGIC;
			Q			: OUT	STD_LOGIC);
END COMPONENT;

COMPONENT Pflop IS
	PORT (Clk, D	: IN	STD_LOGIC;
			Q			: OUT	STD_LOGIC);
END COMPONENT;

BEGIN
	Dlatcha:	Dflop PORT MAP (Clk, D, Qa);
	Platchb:	Pflop PORT MAP (Clk, D, Qb);
	Nlatchc:	Nflop PORT MAP (Clk, D, Qc);
END Behavior;