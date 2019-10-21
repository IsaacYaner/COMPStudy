LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY syncnt8 IS
	PORT (Enable, Clock, Clear	: IN	STD_LOGIC;
			Cout						: OUT STD_LOGIC_VECTOR(7 DOWNTO 0));
END syncnt8;

ARCHITECTURE Behavior of syncnt8 IS

COMPONENT TFFc IS
	PORT (T,CLK,Clear	: IN	STD_LOGIC;
			Q				: OUT	STD_LOGIC);
END COMPONENT;

SIGNAL Ein, Qout : STD_LOGIC_VECTOR(7 DOWNTO 0);

BEGIN
	Ein(0) <= Enable;
	TCount0 : TFFc PORT MAP (Ein(0), Clock, Clear, Qout(0));
G1:FOR i IN 1 to 7 GENERATE
		Ein(i) <= Ein(i-1) AND Qout(i-1);
		TCounti : TFFc PORT MAP (Ein(i), Clock, Clear, Qout(i)); 
	END GENERATE;
	Cout <= Qout;
END Behavior;

--Used 15 LEs, 8 LUT and 7 AND gates.--

--Fmax is 1/propagation dalay of (8 LUT + 7 AND gate)

--The delay is not being larger and larger at 6 nano secs.