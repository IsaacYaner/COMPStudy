LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY MHZ5 IS
	PORT (CLK	: IN	STD_LOGIC;
			Cout	: OUT	STD_LOGIC_VECTOR(3 DOWNTO 0));
END MHZ5;

ARCHITECTURE Behavior OF MHZ5 IS

SIGNAL Enable : STD_LOGIC;

COMPONENT counter10 IS
	PORT (Enable, Cloc, Clear	: IN	STD_LOGIC;
			Cout						: OUT STD_LOGIC_VECTOR(3 DOWNTO 0));
END COMPONENT;

COMPONENT frequencyAdapter IS
	PORT (Cloc		: IN	STD_LOGIC;
			Enable	: OUT STD_LOGIC);
END COMPONENT;

BEGIN
	
	countFor10 : counter10 PORT MAP(Enable, CLK, '0', Cout);
	frenquencyFilter : frequencyAdapter PORT MAP(CLK, Enable);
	
END Behavior;