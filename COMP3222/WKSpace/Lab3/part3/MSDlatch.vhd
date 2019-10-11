LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY MSDlatch IS
	PORT (Clk, D: IN	STD_LOGIC;
			Qs 	: OUT STD_LOGIC);
END MSDlatch;

ARCHITECTURE Behavior OF MSDlatch IS

COMPONENT latchD IS
	PORT (Clk, D : IN STD_LOGIC;
			Q : OUT STD_LOGIC);
END COMPONENT;

SIGNAL Qm : STD_LOGIC;
ATTRIBUTE keep : boolean;
ATTRIBUTE keep OF Qm : SIGNAL IS true;

BEGIN
	MasterLatch : latchD PORT MAP (Clk, D, Qm);
	SlaveLatch  : latchD PORT MAP (NOT(Clk), Qm, Qs);
END Behavior;