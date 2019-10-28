LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY FSMReg IS
	PORT (CLK, w, reset	: IN	STD_LOGIC;
			z					: OUT	STD_LOGIC;
			sequenceStatus : OUT	STD_LOGIC_VECTOR(7 DOWNTO 0));
END FSMReg;

ARCHITECTURE Behavior OF FSMReg IS

COMPONENT shiftReg4bits IS
	PORT (CLK, shiftValue, reset	: IN	STD_LOGIC;
			isAllOne						: OUT	STD_LOGIC;
			status						: OUT STD_LOGIC_VECTOR(3 DOWNTO 0));
END COMPONENT;
			
SIGNAL is0Seq, is1Seq	:	STD_LOGIC;

BEGIN

	register40sequence : shiftReg4bits PORT MAP (CLK, NOT(w), reset, is0Seq, sequenceStatus(7 DOWNTO 4));
	register41sequence : shiftReg4bits PORT MAP (CLK, w,		 reset, is1Seq, sequenceStatus(3 DOWNTO 0));
	z <= is0Seq OR is1Seq;

END Behavior;