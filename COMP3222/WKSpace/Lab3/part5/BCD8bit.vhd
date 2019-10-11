LIBRARY IEEE;
USE ieee.std_logic_1164.all;

ENTITY BCD8bit IS
	PORT (SW		: IN	STD_LOGIC_VECTOR(7 DOWNTO 0);
			KEY	: IN	STD_LOGIC_VECTOR(1 DOWNTO 0);
			HEX0, HEX1, HEX2, HEX3	: OUT	STD_LOGIC_VECTOR(6 DOWNTO 0));
END BCD8bit;

ARCHITECTURE Behavior OF BCD8bit IS

COMPONENT Hnum IS
	PORT (N0					:	OUT	STD_LOGIC_VECTOR(6 DOWNTO 0);
			Cin				:	IN		STD_LOGIC_VECTOR(3 DOWNTO 0));
END COMPONENT;

COMPONENT FF8 IS
	PORT (Cin		: IN 	STD_LOGIC_VECTOR(7 DOWNTO 0);
			Clk, Res	: IN	STD_LOGIC;
			Cout		: OUT	STD_LOGIC_VECTOR(7 DOWNTO 0));
END COMPONENT;

SIGNAL D32, D10 : STD_LOGIC_VECTOR(7 DOWNTO 0);

BEGIN
	latch0 : FF8 PORT MAP (SW(7 DOWNTO 0), KEY(1), KEY(0), D32);
	latch1 : FF8 PORT MAP (SW(7 DOWNTO 0), NOT(KEY(1)), KEY(0), D10);
	Disp3 :	Hnum PORT MAP (Hex3, D32(7 DOWNTO 4));
	Disp2 :	Hnum PORT MAP (Hex2, D32(3 DOWNTO 0));
	Disp1 :	Hnum PORT MAP (Hex1, D10(7 DOWNTO 4));
	Disp0 :	Hnum PORT MAP (Hex0, D10(3 DOWNTO 0));
END Behavior;
