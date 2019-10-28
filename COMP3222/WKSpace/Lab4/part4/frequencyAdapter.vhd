LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY frequencyAdapter IS
	PORT (Cloc			: IN	STD_LOGIC;
			Enable	: OUT STD_LOGIC);
END FrequencyAdapter;

ARCHITECTURE Behavior of FrequencyAdapter IS

SIGNAL Q : STD_LOGIC_VECTOR(25 DOWNTO 0);

BEGIN

	PROCESS(Cloc)
	BEGIN
		IF Cloc'event AND Cloc = '1' THEN
			Q <= Q + 1;
			IF Q = 50000000 THEN
				Q <= (others => '0');
				Enable <= '1';
			ELSE
				Enable <= '0';
			END IF;
		END IF;
	END PROCESS;
END Behavior;

--One LUT and one 16 bit adder--

--1s/7 nano secondes