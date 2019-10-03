LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY mux21 IS
	PORT (U,V	: IN	STD_LOGIC;
			S		: IN	STD_LOGIC;
			W		: OUT	STD_LOGIC);
END mux21;

ARCHITECTURE Behavior OF mux21 IS

BEGIN
	W <= (S AND V) OR (NOT(S) AND U);
END Behavior;