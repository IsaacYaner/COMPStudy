LIBRARY ieee; 
USE ieee.std_logic_1164.all;
USE ieee.std_logic_signed.all;

ENTITY part1 IS
	PORT (DIN : IN STD_LOGIC_VECTOR(8 DOWNTO 0);
			Resetn, Clock, Run : IN STD_LOGIC;
			Done : BUFFER STD_LOGIC;
			BusWires : BUFFER STD_LOGIC_VECTOR(8 DOWNTO 0));
END part1;

ARCHITECTURE Behavior OF part1 IS
	-- declare components
	COMPONENT dec3to8 IS
		PORT (W : IN STD_LOGIC_VECTOR(2 DOWNTO 0);
				En : IN STD_LOGIC;
				Y : OUT STD_LOGIC_VECTOR(0 TO 7));
	END COMPONENT;
	
	COMPONENT regn IS
		GENERIC (n : INTEGER := 9);
		PORT (R : IN STD_LOGIC_VECTOR(n-1 DOWNTO 0);
				Rin, Clock : IN STD_LOGIC;
				Q : BUFFER STD_LOGIC_VECTOR(n-1 DOWNTO 0));
	END COMPONENT;
	
	COMPONENT addsubUnit IS
		PORT (summand0 : IN  STD_LOGIC_VECTOR(8 DOWNTO 0);
				summand1 : IN  STD_LOGIC_VECTOR(8 DOWNTO 0);
				Result 	: OUT STD_LOGIC_VECTOR(8 DOWNTO 0);
				instruction : IN STD_LOGIC); -- instruction = 1 means add vice versa.
	END COMPONENT;
	-- declare signals
	TYPE State_type IS (T0, T1, T2, T3);
	SIGNAL Tstep_Q, Tstep_D: State_type;
	SIGNAL Hi, IRin, Dinout, Ain, Gin, Gout, AddSub : STD_LOGIC;
	SIGNAL I : STD_LOGIC_VECTOR(2 DOWNTO 0);
	SIGNAL Xreg, Yreg, Rin, Rout : STD_LOGIC_VECTOR(7 DOWNTO 0);
	SIGNAL IR, A, G, AddResult : STD_LOGIC_VECTOR(8 DOWNTO 0);
	TYPE RegArray IS array (0 to 7) OF STD_LOGIC_VECTOR(8 DOWNTO 0);
	SIGNAL R	:	RegArray;
	
BEGIN
	Hi <= '1';
	I <= IR(8 DOWNTO 6);
	decX: dec3to8 PORT MAP (IR(5 DOWNTO 3), Hi, Xreg);
	decY: dec3to8 PORT MAP (IR(2 DOWNTO 0), Hi, Yreg);

	statetable: PROCESS (Tstep_Q, Run, Done)
	BEGIN
		CASE Tstep_Q IS
			WHEN T0 => -- data is loaded into IR in this time step
				IF (Run = '0') THEN
					Tstep_D <= T0;
				ELSE 
					Tstep_D <= T1;
				END IF; 
			WHEN T1 => -- executing step table
				IF (Done = '1') THEN
					Tstep_D <= T0;
				ELSE 
					Tstep_D <= T2;
				END IF;
			WHEN T2 =>
				IF (Done = '1') THEN
					Tstep_D <= T0;
				ELSE 
					Tstep_D <= T3;
				END IF;
			WHEN others =>
				Tstep_D <= T0;
		END CASE;
	END PROCESS;

	controlsignals: PROCESS (Tstep_Q, I, Xreg, Yreg)
	BEGIN
		-- specify initial values
		Ain <= '0'; Rin <= "00000000"; Rout <= "00000000"; Done <= '0';
		Gin <= '0'; Dinout <= '0'; IRin <= '0'; AddSub <= '0'; Gout <= '0';
		CASE Tstep_Q IS
			WHEN T0 => -- store DIN in IR as long as Tstep_Q = 0
				IRin <= '1';
			WHEN T1 => -- define signals in time step T1
				CASE I IS
					WHEN "000" =>
						Rin  <= Xreg;
						Rout <= Yreg;
						Done <= '1';
						
					WHEN "001" =>
						Rin  <= Xreg;
						Dinout <= '1';
						Done <= '1';
					
					WHEN "010" | "011" =>
						Ain  <= '1';
						Rout <= Xreg;
						
					WHEN others =>
				END CASE;
			WHEN T2 => -- define signals in time step T2
				CASE I IS
					WHEN "010" =>
						Rout <= Yreg;
						Gin  <= '1';
						
					WHEN "011" =>
						Rout <= Yreg;
						Gin  <= '1';
						AddSub <= '1';
						
					WHEN others =>
				END CASE;
			WHEN T3 => -- define signals in time step T3
				CASE I IS
					WHEN "010" | "011" =>
						Gout <= '1';
						Rin  <= Xreg;
						Done <= '1';
						
					WHEN others =>
				END CASE;
		END CASE;
	END PROCESS;

	fsmflipflops: PROCESS (Clock, Resetn)
	BEGIN
		IF resetn = '0' THEN
			Tstep_Q <= T0;
		ELSIF Clock'event AND Clock = '1' THEN
			Tstep_Q <= Tstep_D;
		END IF;
		
--		IF resetn = '0' THEN 			--Or use ELSIF Clock'event?
--			Tstep_Q <= T0;
--		END IF;
	END PROCESS;
	
GENREG:	
	FOR i IN 0 TO 7 GENERATE
		regiIn	: regn PORT MAP (BUSWires, Rin(i), Clock, R(i));			-- Write into Reg
	END GENERATE;
		regAin   : regn PORT MAP (BUSWires, Ain,    Clock, A);
		regGin	: regn PORT MAP (AddResult,Gin,	  Clock, G);
		regIRin  : regn PORT MAP (DIN, 		IRin,   Clock, IR);
		
	AdderSubstracterUnit : addsubUnit PORT mAP (A, BUSWires, AddResult, AddSub);
	-- instantiate registers and the adder/subtracter unit
	
	PROCESS (Rout, Dinout, Gout, Clock)
	BEGIN
		IF Clock'event AND Clock = '1' THEN		--Could I use loop to achieve that?
			IF Rout(0) = '1' THEN
				BUSWires <= R(0);
			ELSIF Rout(1) = '1' THEN
				BUSWires <= R(1);
			ELSIF Rout(2) = '1' THEN
				BUSWires <= R(2);
			ELSIF Rout(3) = '1' THEN
				BUSWires <= R(3);
			ELSIF Rout(4) = '1' THEN
				BUSWires <= R(4);
			ELSIF Rout(5) = '1' THEN
				BUSWires <= R(5);
			ELSIF Rout(6) = '1' THEN
				BUSWires <= R(6);
			ELSIF Rout(7) = '1' THEN
				BUSWires <= R(7);
			ELSIF Gout = '1' THEN
				BUSWires <= G;
			ELSIF Dinout = '1' THEN
				BUSWires <= Din;
			END IF;
		END IF;
	END PROCESS;
	-- define the bus

END Behavior;


LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY addsubUnit IS
	PORT (summand0 : IN  STD_LOGIC_VECTOR(8 DOWNTO 0);
			summand1 : IN  STD_LOGIC_VECTOR(8 DOWNTO 0);
			Result 	: OUT STD_LOGIC_VECTOR(8 DOWNTO 0);
			instruction : IN STD_LOGIC); -- instruction = 1 means add vice versa.
END addsubUnit;

ARCHITECTURE Behavior OF addsubUnit IS
BEGIN
	Result <= summand0 + summand1 WHEN instruction = '1' ELSE summand0 - summand1;
END Behavior;

LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY dec3to8 IS
	PORT (W : IN STD_LOGIC_VECTOR(2 DOWNTO 0);
			En : IN STD_LOGIC;
			Y : OUT STD_LOGIC_VECTOR(0 TO 7));
END dec3to8;

ARCHITECTURE Behavior OF dec3to8 IS
BEGIN
	PROCESS (W, En)
	BEGIN
		IF (En = '1') THEN
			CASE W IS	
				WHEN "000" => Y <= "10000000";
				WHEN "001" => Y <= "01000000";
				WHEN "010" => Y <= "00100000";
				WHEN "011" => Y <= "00010000";
				WHEN "100" => Y <= "00001000";
				WHEN "101" => Y <= "00000100";
				WHEN "110" => Y <= "00000010";
				WHEN "111" => Y <= "00000001";
			END CASE;
		ELSE
			Y <= "00000000";
		END IF;
	END PROCESS;
END Behavior;

LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY regn IS
	GENERIC (n : INTEGER := 9);
	PORT (R : IN STD_LOGIC_VECTOR(n-1 DOWNTO 0);
			Rin, Clock : IN STD_LOGIC;
			Q : BUFFER STD_LOGIC_VECTOR(n-1 DOWNTO 0));
END regn;

ARCHITECTURE Behavior OF regn IS
BEGIN
	PROCESS (Clock)
	BEGIN
		IF (rising_edge(Clock)) THEN
			IF (Rin = '1') THEN
				Q <= R;
			END IF;
		END IF;
	END PROCESS;
END Behavior;