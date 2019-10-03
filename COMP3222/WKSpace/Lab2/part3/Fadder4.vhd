LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY Fadder4 IS
	PORT (a, b	: IN	STD_LOGIC_VECTOR(3 DOWNTO 0);
			cin	: IN	STD_LOGIC						 ;
			s		: OUT STD_LOGIC_VECTOR(3 DOWNTO 0); 
			cout	: OUT	STD_LOGIC						);
END Fadder4;

ARCHITECTURE Behavior OF Fadder4 IS

COMPONENT Fadder IS
	PORT (a, b, cin	: IN	STD_LOGIC;
			s, cout		: OUT	STD_LOGIC);
END COMPONENT;

SIGNAL c : STD_LOGIC_VECTOR(2 DOWNTO 0);

BEGIN
	Add0 : Fadder PORT MAP (a(0), b(0), cin,  s(0), c(0));
	Add1 : Fadder PORT MAP (a(1), b(1), c(0), s(1), c(1));
	Add2 : Fadder PORT MAP (a(2), b(2), c(1), s(2), c(2));
	Add3 : Fadder PORT MAP (a(3), b(3), c(2), s(3), cout);
END Behavior;