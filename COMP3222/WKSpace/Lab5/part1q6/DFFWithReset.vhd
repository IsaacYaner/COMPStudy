LIBRARY ieee ;
USE ieee.std_logic_1164.all;

ENTITY Dflop IS
	PORT (Clk, D, reset	: IN	STD_LOGIC;
			Q					: OUT	STD_LOGIC);
END Dflop;

ARCHITECTURE Behavior OF Dflop IS
BEGIN

	PROCESS(D, Clk, reset)
	BEGIN
		IF Clk'event AND Clk = '1' THEN
			IF reset = '0' THEN
				Q <= '0';
			ELSE
				Q <= D;
			END IF;
		END IF;
	END PROCESS;

END Behavior;