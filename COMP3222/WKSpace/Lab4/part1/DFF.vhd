LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY TFFc IS
	PORT (T,CLK,Clear	: IN	STD_LOGIC;
			Q				: OUT	STD_LOGIC);
END TFFc;

ARCHITECTURE Behavior of TFFc IS

--Initial value of TFF?

SIGNAL outPut : STD_LOGIC;

BEGIN
	PROCESS(CLK, Clear)
	BEGIN
		IF Clear = '1' THEN
			outPut <= '0';
		ELSIF CLK'event AND (CLK = '1') AND (T = '1') THEN
			outPut <= NOT(outPut);
		END IF;
	END PROCESS;
	Q <= outPut;
END Behavior;