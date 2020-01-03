LIBRARY IEEE;
USE ieee.std_logic_1164.all;

ENTITY part2 IS 
	PORT (MClock, PClock, Resetn, Run	: IN	STD_LOGIC;
			BUSWires								: OUT STD_LOGIC_VECTOR(8 DOWNTO 0);
			Done									: OUT STD_LOGIC);
END part2;

ARCHITECTURE Behavior OF part2 IS

COMPONENT counter IS 
	GENERIC (N	:	INTEGER);
	PORT (Clock 	: IN	STD_LOGIC;
			Number	: OUT STD_LOGIC_VECTOR(N-1 DOWNTO 0));
END COMPONENT;

COMPONENT part1 IS
	PORT (DIN : IN STD_LOGIC_VECTOR(8 DOWNTO 0);
			Resetn, Clock, Run : IN STD_LOGIC;
			Done : BUFFER STD_LOGIC;
			BusWires : BUFFER STD_LOGIC_VECTOR(8 DOWNTO 0));
END COMPONENT;

COMPONENT inst_mem IS
	PORT
	(
		address		: IN STD_LOGIC_VECTOR (4 DOWNTO 0);
		clock			: IN STD_LOGIC  := '1';
		q				: OUT STD_LOGIC_VECTOR (8 DOWNTO 0)
	);
END COMPONENT;

SIGNAL address_for_mem : STD_LOGIC_VECTOR(4 DOWNTO 0);
SIGNAL DIN : STD_LOGIC_VECTOR(8 DOWNTO 0);

BEGIN
	Counter0	: counter GENERIC MAP (N => 5) PORT MAP (MClock, address_for_mem);
	Memory 	: inst_mem PORT MAP (address_for_mem, MClock, DIN);
	Processor: part1 PORT MAP (DIN, Resetn, PClock, Run, Done, BUSWires);
END Behavior;