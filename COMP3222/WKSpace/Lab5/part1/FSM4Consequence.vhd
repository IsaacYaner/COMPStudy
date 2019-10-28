LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY FSM4Consequence IS
	PORT (w,	CLK, reset	: IN	STD_LOGIC;
			z					: OUT	STD_LOGIC;
			stateOut			: OUT	STD_LOGIC_VECTOR(8 DOWNTO 0));
END FSM4Consequence;

ARCHITECTURE Behavior OF FSM4Consequence IS

COMPONENT Dflop IS
	PORT (Clk, D	: IN	STD_LOGIC;
			Q			: OUT	STD_LOGIC);
END COMPONENT;

SIGNAL state		:	STD_LOGIC_VECTOR(8 DOWNTO 0);
SIGNAL nextState	:	STD_LOGIC_VECTOR(8 DOWNTO 0);

BEGIN

	z <= state(4) OR state(8);			--Assign value for output
	
	nextState(0) <=  NOT(reset);				--Calculate nextStates and synchronous active-Low reset
	
	nextState(1) <= (state(0) OR state(5) OR state(6) OR state(7) OR state(8)) AND NOT(w) AND reset;
	nextState(2) <=  state(1) AND NOT(w) AND reset;
	nextState(3) <=  state(2) AND NOT(w) AND reset;
	nextState(4) <= (state(3) OR state(4)) AND NOT(w) AND reset;
	nextState(5) <= (state(0) OR state(1) OR state(2) OR state(3) OR state(4)) AND w AND reset;
	nextState(6) <=  state(5) AND w AND reset;
	nextState(7) <=  state(6) AND w AND reset;
	nextState(8) <= (state(7) OR state(8)) AND w AND reset;
	
	generateNextState : 
	FOR i IN 0 to 8 GENERATE
		RealiseNextState : Dflop PORT MAP (CLK, nextState(i), state(i));
	END GENERATE;

	stateOut <= state;
	
END Behavior;