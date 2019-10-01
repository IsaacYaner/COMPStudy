LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY part5 IS
	PORT (SW : IN STD_LOGIC_VECTOR(9 DOWNTO 0);
			HEX0 : OUT STD_LOGIC_VECTOR(0 TO 6));
END part5;

ARCHITECTURE Behavior OF part5 IS

COMPONENT mux_2bit_3to1
	PORT (S, U, V, W : IN STD_LOGIC_VECTOR(1 DOWNTO 0);
			M : OUT STD_LOGIC_VECTOR(1 DOWNTO 0));
END COMPONENT;

COMPONENT char_7seg
	PORT (C : IN STD_LOGIC_VECTOR(1 DOWNTO 0);
			Display : OUT STD_LOGIC_VECTOR(0 TO 6));
END COMPONENT;

SIGNAL M : STD_LOGIC_VECTOR(1 DOWNTO 0);

BEGIN
	M0: mux_2bit_3to1 PORT MAP (SW(9 DOWNTO 8), SW(5 DOWNTO 4), SW(3 DOWNTO 2),
	SW(1 DOWNTO 0), M);
	H0: char_7seg PORT MAP (M, HEX0);
END Behavior;
















LIBRARY ieee;
USE ieee.std_logic_1164.all;

-- implements a 2-bit wide 3-to-1 multiplexer
ENTITY mux_2bit_3to1 IS
	PORT (S, U, V, W : IN STD_LOGIC_VECTOR(1 DOWNTO 0);
			M : OUT STD_LOGIC_VECTOR(1 DOWNTO 0));
END mux_2bit_3to1;

ARCHITECTURE Behavior OF mux_2bit_3to1 IS


SIGNAL T : STD_LOGIC_VECTOR(1 DOWNTO 0);

BEGIN
	T(1) <= (NOT(S(0)) AND U(1)) OR (S(0) AND V(1));
	T(0) <= (NOT(S(0)) AND U(0)) OR (S(0) AND V(0));
	M(1) <= (NOT(S(1)) AND T(1)) OR (S(1) AND W(1));
	M(0) <= (NOT(S(1)) AND T(0)) OR (S(1) AND W(0));
END Behavior;

LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY char_7seg IS
	PORT (C : IN STD_LOGIC_VECTOR(1 DOWNTO 0);
			Display : OUT STD_LOGIC_VECTOR(0 TO 6));
END char_7seg;

ARCHITECTURE Behavior OF char_7seg IS

BEGIN
	Display(0)<=not(not(C(1)) and C(0));--Is the bracket necessary?
	Display(1)<=(C(0));
	Display(2)<=(C(0));
	Display(3)<=(C(1));
	Display(4)<=(C(1));
	Display(5)<=not(not(C(1)) and C(0));
	Display(6)<=(C(1));
END Behavior;