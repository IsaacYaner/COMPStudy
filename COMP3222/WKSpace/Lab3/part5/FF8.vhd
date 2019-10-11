LIBRARY IEEE;
USE ieee.std_logic_1164.all;

--Flip flop for one bit.
ENTITY FF8 IS
	PORT (Cin		: IN 	STD_LOGIC_VECTOR(7 DOWNTO 0);
			Clk, Res	: IN	STD_LOGIC;
			Cout		: OUT	STD_LOGIC_VECTOR(7 DOWNTO 0));
END FF8;

ARCHITECTURE Behavior OF FF8 IS

BEGIN
	PROCESS(Clk, Res)
	BEGIN
		IF Res = '0' THEN
			Cout <= "00000000";
		ELSIF CLK'event AND CLK = '1' THEN
			Cout <= Cin;
		END IF;
	END PROCESS;
END Behavior;
