LIBRARY ieee ;
USE ieee.std_logic_1164.all;

ENTITY Pflop IS
	PORT (Clk, D	: IN	STD_LOGIC;
			Q			: OUT	STD_LOGIC);
END Pflop;

ARCHITECTURE Behavior OF Pflop IS

BEGIN

	PROCESS(D, Clk)
	BEGIN
		IF CLK'event AND CLK = '1' THEN
			Q <= D;
		END IF;
	END PROCESS;

END Behavior;