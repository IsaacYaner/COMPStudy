LIBRARY ieee ;
USE ieee.std_logic_1164.all;

ENTITY part1 IS
	PORT (SW		: IN	STD_LOGIC_VECTOR(1 DOWNTO 0);
			KEY	: IN	STD_LOGIC_VECTOR(0 DOWNTO 0);
			LEDG	: OUT STD_LOGIC_VECTOR(0 DOWNTO 0);
			LEDR	: OUT	STD_LOGIC_VECTOR(8 DOWNTO 0));
END part1;

ARCHITECTURE Behavior OF part1 IS

COMPONENT FSM4Consequence IS
	PORT (w,	CLK, reset	: IN	STD_LOGIC;
			z					: OUT	STD_LOGIC;
			stateOut			: OUT	STD_LOGIC_VECTOR(8 DOWNTO 0));
END COMPONENT;

BEGIN
	
	simulateToBoard : FSM4Consequence PORT MAP (SW(1), KEY(0), SW(0), LEDG(0), LEDR);
	
END Behavior;