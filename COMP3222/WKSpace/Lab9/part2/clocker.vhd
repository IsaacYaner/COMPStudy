LIBRARY IEEE;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY counter IS
	GENERIC (N	:	INTEGER);
	PORT (Clock 	: IN	STD_LOGIC;
			Number	: OUT STD_LOGIC_VECTOR(N-1 DOWNTO 0));
END counter;

ARCHITECTURE Behavior OF counter IS 

SIGNAL count : STD_LOGIC_VECTOR(N-1 DOWNTO 0);

BEGIN
	PROCESS(Clock)
	BEGIN
		IF Clock'event AND Clock = '1' THEN
			count <= count + 1;
		END IF;
	END PROCESS;
	Number <= count;
END Behavior;