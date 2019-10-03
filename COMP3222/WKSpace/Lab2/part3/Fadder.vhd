LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY Fadder IS
	PORT (a, b, cin	: IN	STD_LOGIC;
			s, cout		: OUT	STD_LOGIC);
END Fadder;

ARCHITECTURE Behavior OF Fadder IS

COMPONENT mux21 IS
	PORT (U,V	: IN	STD_LOGIC;
			S		: IN	STD_LOGIC;
			W		: OUT	STD_LOGIC);
END COMPONENT;

BEGIN
	s <= cin XOR (a XOR b);
	Carry : mux21 PORT MAP (b, cin, (a xor b), cout);
	
END Behavior;