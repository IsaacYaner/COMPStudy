LIBRARY ieee ;
USE ieee.std_logic_1164.all;

ENTITY Dflop IS
	PORT (Clk, D	: IN	STD_LOGIC;
			Q			: OUT	STD_LOGIC);
END Dflop;

ARCHITECTURE Behavior OF Dflop IS
BEGIN

	PROCESS(D, Clk)
	BEGIN
		IF Clk = '1' THEN
			Q <= D;
		END IF;
	END PROCESS;

END Behavior;