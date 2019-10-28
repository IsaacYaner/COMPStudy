LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY part3 IS
	PORT (SW		: IN	STD_LOGIC_VECTOR(1 DOWNTO 0);
			KEY	: IN	STD_LOGIC_VECTOR(0 DOWNTO 0);
			LEDG	: OUT STD_LOGIC_VECTOR(0 DOWNTO 0);
			LEDR	: OUT STD_LOGIC_VECTOR(7 DOWNTO 0));
END part3;

ARCHITECTURE Behavior OF part3 IS

COMPONENT FSMReg IS
	PORT (CLK, w, reset	: IN	STD_LOGIC;
			z					: OUT	STD_LOGIC;
			sequenceStatus : OUT	STD_LOGIC_VECTOR(7 DOWNTO 0));
END COMPONENT;

BEGIN

	recogniseSequence : FSMReg PORT MAP (KEY(0), SW(1), SW(0), LEDG(0), LEDR);

END Behavior;