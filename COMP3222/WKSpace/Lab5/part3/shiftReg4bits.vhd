LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY shiftReg4bits IS
	PORT (CLK, shiftValue, reset	: IN	STD_LOGIC;
			isAllOne						: OUT	STD_LOGIC;
			status						: OUT STD_LOGIC_VECTOR(3 DOWNTO 0));
END shiftReg4bits;

ARCHITECTURE Behavior OF shiftReg4bits IS

SIGNAL data : STD_LOGIC_VECTOR(3 DOWNTO 0);

BEGIN

	PROCESS(CLK)
	BEGIN
		IF CLK'event AND CLK = '1' THEN
			IF reset = '0' THEN
				data(3) <= '0';
				data(2) <= '0';
				data(1) <= '0';
				data(0) <= '0';
			ELSE
				data(3) <= data(2);
				data(2) <= data(1);
				data(1) <= data(0);
				data(0) <= shiftValue;
			END IF;
		END IF;
	END PROCESS;
	
	status <= data;
	isAllOne <= data(3) AND data(2) AND data(1) AND data(0);
END Behavior;