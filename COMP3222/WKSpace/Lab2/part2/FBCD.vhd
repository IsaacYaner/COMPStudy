LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY FBCD IS
	PORT (SW				: IN	STD_LOGIC_VECTOR(4 DOWNTO 0);
			HEX0, HEX1	: OUT	STD_LOGIC_VECTOR(6 DOWNTO 0);
			Err			: OUT	STD_LOGIC						);
END FBCD;

ARCHITECTURE Behavior OF FBCD IS

SIGNAL z		:	STD_LOGIC;
SIGNAL V1	:	STD_LOGIC_VECTOR(3 DOWNTO 0);	--The values after reducing.
SIGNAL W1	:	STD_LOGIC_VECTOR(3 DOWNTO 0); --Another value after reducing.
SIGNAL P1	:	STD_LOGIC_VECTOR(3 DOWNTO 0); --True values we expect.
SIGNAL M		:	STD_LOGIC_VECTOR(3 DOWNTO 0); 
SIGNAL Z1	:	STD_LOGIC_VECTOR(3 DOWNTO 0);

COMPONENT CirA IS
	PORT (V				: IN	STD_LOGIC_VECTOR(2 DOWNTO 0);
			M				: OUT	STD_LOGIC_VECTOR(2 DOWNTO 0));
END COMPONENT;

COMPONENT cmptr IS
	PORT (V				: IN	STD_LOGIC_VECTOR(3 DOWNTO 0);
			Z				: OUT	STD_LOGIC);
END COMPONENT;

COMPONENT mux214 IS
	PORT (U,V	: IN	STD_LOGIC_VECTOR(3 DOWNTO 0);
			S		: IN	STD_LOGIC;
			W		: OUT	STD_LOGIC_VECTOR(3 DOWNTO 0));
END COMPONENT;

COMPONENT numb IS
	PORT (N0					:	OUT	STD_LOGIC_VECTOR(6 DOWNTO 0);
			Cin				:	IN		STD_LOGIC_VECTOR(3 DOWNTO 0));
END COMPONENT;

COMPONENT CirC IS
	PORT (V				: IN	STD_LOGIC_VECTOR(3 DOWNTO 0);
			M				: OUT	STD_LOGIC_VECTOR(3 DOWNTO 0));
END COMPONENT;

BEGIN
	IFTEN : cmptr  PORT MAP (SW(3 DOWNTO 0), z);
	CircA : CirA   PORT MAP (SW(2 DOWNTO 0), V1(2 DOWNTO 0));
	CircC	: CirC	PORT MAP (SW(3 DOWNTO 0), W1(3 DOWNTO 0));
	Err <= SW(4) AND (SW(3) OR SW(2));
	V1(3) <= '0';
	Z1(3) <= '0';
	Z1(2) <= '0';
	Z1(1) <= '0';
	Z1(0) <= z OR SW(4);												-- Is there a better to assign values?
	MUX0	: mux214 PORT MAP (V1, W1, SW(4), P1);	-- Choose Value for alternative according to the highest bit.
	MUX1	: mux214 PORT MAP (SW(3 DOWNTO 0), P1, Z1(0), M);
	H1		: numb	PORT MAP (HEX1, Z1); 			-- Is there a better way to pass the value?
	H0		: numb	PORT MAP (HEX0, M);
END Behavior;