LIBRARY IEEE;
USE ieee.std_logic_1164.all;

ENTITY part1 IS
	PORT (SW		: IN	STD_LOGIC_VECTOR(8 DOWNTO 0);
			KEY	: IN	STD_LOGIC_VECTOR(1 DOWNTO 0);
			CLOCK_50 : IN STD_LOGIC;
			LEDR	: OUT	STD_LOGIC_VECTOR(7 DOWNTO 0);
			LEDG	: OUT	STD_LOGIC_VECTOR(0 DOWNTO 0)
			);
END part1;

ARCHITECTURE Behavior OF part1 IS

COMPONENT CounterFSM IS
	GENERIC(N : NATURAL := 8);
	PORT (Cin	 : IN	 STD_LOGIC_VECTOR(N-1 DOWNTO 0);
			s		 : IN	 STD_LOGIC;
			Resetn : IN	 STD_LOGIC;
			CLK	 : IN  STD_LOGIC;
			Cout	 : OUT STD_LOGIC_VECTOR(N-1 DOWNTO 0);
			Done	 : OUT STD_LOGIC);
END COMPONENT;

BEGIN
	instCounter : CounterFSM PORT MAP (SW(7 DOWNTO 0), SW(8), KEY(0), KEY(1), LEDR(7 DOWNTO 0), LEDG(0));
END Behavior;