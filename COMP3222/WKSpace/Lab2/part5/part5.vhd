LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.numeric_std.all;

ENTITY part5 IS
	PORT (SW								: IN	STD_LOGIC_VECTOR(8 DOWNTO 0);
			HEX3, HEX2, HEX1, HEX0	: OUT STD_LOGIC_VECTOR(6 DOWNTO 0);
			LEDG							: OUT STD_LOGIC_VECTOR(7 DOWNTO 0));
END part5;


ARCHITECTURE Behavior OF part5 IS

SIGNAL A, B, cin, cout, T, Z, S0, S1, S3: INTEGER;
SIGNAL Sum : STD_LOGIC_VECTOR(4 DOWNTO 0);

COMPONENT FBCD IS 
	PORT (SW				: IN	STD_LOGIC_VECTOR(4 DOWNTO 0);
			HEX0, HEX1	: OUT	STD_LOGIC_VECTOR(6 DOWNTO 0);
			Err			: OUT STD_LOGIC						);
END COMPONENT;

COMPONENT numb IS
	PORT (N0					:	OUT	STD_LOGIC_VECTOR(6 DOWNTO 0);
			Cin				:	IN		STD_LOGIC_VECTOR(3 DOWNTO 0));
END COMPONENT;

BEGIN
	A <= to_integer(unsigned(SW(7 DOWNTO 4)));
	B <= to_integer(unsigned(SW(3 DOWNTO 0)));
	cin <= 1 when (SW(8) = '1') else 0;
	PROCESS(A, B, cin, cout, T, Z, S0, S1, S3)
	BEGIN
		T <= A + B + cin;
		IF (T > 9) THEN
			Z <= 10;
			cout <= 1;
		ELSE
			Z <= 0;
			cout <= 0;
		END IF;
		S0 <= T - Z;
		S1 <= cout;
		S3 <= S0 + S1 * 10;
	END PROCESS;
	Sum <= STD_LOGIC_VECTOR(to_unsigned(S3, 5));
	Disp0 : numb  PORT MAP (HEX3, SW(7 DOWNTO 4));
	Disp1 : numb  PORT MAP (HEX2, SW(3 DOWNTO 0));
	Disp2 : FBCD  PORT MAP (Sum , HEX0, HEX1, LEDG(7));
	------------------------HOW TO USE THE RTL VIEWER??????????????????????
END Behavior;