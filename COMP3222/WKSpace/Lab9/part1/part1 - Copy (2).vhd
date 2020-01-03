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
				AddSub : IN STD_LOGIC); -- instruction = 1 means add vice versa.
	END COMPONENT;
	-- declare signals
	TYPE State_type IS (T0, T1, T2, T3);
	SIGNAL Tstep_Q, Tstep_D: State_type;
	SIGNAL Hi, IRin, Ain, Gin, AddSub : STD_LOGIC;
	SIGNAL I : STD_LOGIC_VECTOR(2 DOWNTO 0);
	SIGNAL Xreg, Rin : STD_LOGIC_VECTOR(7 DOWNTO 0);
   SIGNAL R0, R1, R2, R3, R4, R5, R6, R7 : STD_LOGIC_VECTOR(8 DOWNTO 0);
	SIGNAL IR, A, G, AddResult : STD_LOGIC_VECTOR(8 DOWNTO 0);
		CONSTANT OutR0 : STD_LOGIC_VECTOR(3 DOWNTO 0) := "0000";
		CONSTANT OutR1 : STD_LOGIC_VECTOR(3 DOWNTO 0) := "0001";
		CONSTANT OutR2 : STD_LOGIC_VECTOR(3 DOWNTO 0) := "0010";
		CONSTANT OutR3 : STD_LOGIC_VECTOR(3 DOWNTO 0) := "0011";
		CONSTANT OutR4 : STD_LOGIC_VECTOR(3 DOWNTO 0) := "0100";
		CONSTANT OutR5 : STD_LOGIC_VECTOR(3 DOWNTO 0) := "0101";
		CONSTANT OutR6 : STD_LOGIC_VECTOR(3 DOWNTO 0) := "0110";
		CONSTANT OutR7 : STD_LOGIC_VECTOR(3 DOWNTO 0) := "0111";
		CONSTANT OutG  : STD_LOGIC_VECTOR(3 DOWNTO 0) := "1000";
		CONSTANT OutD  : STD_LOGIC_VECTOR(3 DOWNTO 0) := "1001";
		SIGNAL outoBus : STD_LOGIC_VECTOR(3 DOWNTO 0); -- bus selector

BEGIN
	Hi <= '1';
	I <= IR(8 DOWNTO 6);
	decX: dec3to8 PORT MAP (IR(5 DOWNTO 3), Hi, Xreg);

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
				Tstep_D <= T3;
			WHEN T3 =>
				Tstep_D <= T0;
		END CASE;
	END PROCESS;

	controlsignals: PROCESS (Tstep_Q, I, Xreg, IR)
	BEGIN
		-- specify initial values
		Ain <= '0'; Rin <= "00000000"; Done <= '0';
		Gin <= '0'; IRin <= '0'; AddSub <= '0';
		outoBus <= (others => '0');
		CASE Tstep_Q IS
			WHEN T0 => -- store DIN in IR as long as Tstep_Q = 0
				IRin <= '1';
			WHEN T1 => -- define signals in time step T1
				CASE I IS
					WHEN "000" =>
						Rin  <= Xreg;
						outoBus <= '0' & IR(2 DOWNTO 0);
						Done <= '1';
						
					WHEN "001" =>
						Rin  <= Xreg;
						outoBus <= OutD;
						Done <= '1';
					
					WHEN "010" | "011" =>
						Ain  <= '1';
						outoBus <= '0' & IR(5 DOWNTO 3);
						
					WHEN others =>
				END CASE;
			WHEN T2 => -- define signals in time step T2
				CASE I IS
					WHEN "010" =>
						outoBus <= '0' & IR(2 DOWNTO 0);
						Gin  <= '1';
						
					WHEN "011" =>
						outoBus <= '0' & IR(2 DOWNTO 0);
						Gin  <= '1';
						AddSub <= '1';
						
					WHEN others =>
				END CASE;
			WHEN T3 => -- define signals in time step T3
				CASE I IS
					WHEN "010" | "011" =>
						outoBus <= outG;
						Rin  <= Xreg;
						Done <= '1';
						
					WHEN others =>
				END CASE;
		END CASE;
	END PROCESS;

	fsmflipflops: PROCESS (Clock, Resetn)
	BEGIN
		IF Resetn = '0' THEN
			Tstep_Q <= T0;
		ELSIF Clock'event AND Clock = '1' THEN
			Tstep_Q <= Tstep_D;
		END IF;
		
--		IF resetn = '0' THEN 			--Or use ELSIF Clock'event?
--			Tstep_Q <= T0;
--		END IF;
	END PROCESS;
	
--GENREG:	
--	FOR i IN 0 TO 7 GENERATE
--		regiIn	: regn PORT MAP (BUSWires, Rin(i), Clock, R(i));			-- Write into Reg
--	END GENERATE;
		reg_0 	: regn PORT MAP (BusWires, Rin(0), Clock, R0);
		reg_1 	: regn PORT MAP (BusWires, Rin(1), Clock, R1);
		reg_2 	: regn PORT MAP (BusWires, Rin(2), Clock, R2);
		reg_3 	: regn PORT MAP (BusWires, Rin(3), Clock, R3);
		reg_4 	: regn PORT MAP (BusWires, Rin(4), Clock, R4);
		reg_5 	: regn PORT MAP (BusWires, Rin(5), Clock, R5);
		reg_6 	: regn PORT MAP (BusWires, Rin(6), Clock, R6);
		reg_7 	: regn PORT MAP (BusWires, Rin(7), Clock, R7);
		
		regA	   : regn PORT MAP (BUSWires, Ain,    Clock, A);
		regIR	   : regn PORT MAP (DIN, 		IRin,   Clock, IR);
		
	--AdderSubstracterUnit : addsubUnit PORT mAP (A, BUSWires, AddResult, AddSub);
		PROCESS (AddSub, A, BUSWires)
		BEGIN
        IF AddSub = '0' THEN
            AddResult <= A + BUSWires;
        ELSE
            AddResult <= A - BUSWires;
        END IF;
		END PROCESS;
		regG		: regn PORT MAP (AddResult,Gin,	  Clock, G);
	-- instantiate registers and the adder/subtracter unit
	
    PROCESS (outoBus, R0, R1, R2, R3, R4, R5, R6, R7, G, IR, Din)
    BEGIN
        CASE outoBus IS
            WHEN OutR0 => BusWires <= R0;
            WHEN OutR1 => BusWires <= R1;
            WHEN OutR2 => BusWires <= R2;
            WHEN OutR3 => BusWires <= R3;
            WHEN OutR4 => BusWires <= R4;
            WHEN OutR5 => BusWires <= R5;
            WHEN OutR6 => BusWires <= R6;
            WHEN OutR7 => BusWires <= R7;
            WHEN OutG  => BusWires <= G;
            WHEN OutD  => BusWires <= Din;
            WHEN OTHERS => BusWires <= (OTHERS => '-');
        END CASE;
    END PROCESS;   	
	
--	PROCESS (Rout, Dinout, Gout, Clock)
--	BEGIN
--		IF Clock'event AND Clock = '1' THEN		--Could I use loop to achieve that?
--			IF Rout(0) = '1' THEN
--				BUSWires <= R0;
--			ELSIF Rout(1) = '1' THEN
--				BUSWires <= R1;
--			ELSIF Rout(2) = '1' THEN
--				BUSWires <= R2;
--			ELSIF Rout(3) = '1' THEN
--				BUSWires <= R3;
--			ELSIF Rout(4) = '1' THEN
--				BUSWires <= R4;
--			ELSIF Rout(5) = '1' THEN
--				BUSWires <= R5;
--			ELSIF Rout(6) = '1' THEN
--				BUSWires <= R6;
--			ELSIF Rout(7) = '1' THEN
--				BUSWires <= R7;
--			ELSIF Gout = '1' THEN
--				BUSWires <= G;
--			ELSIF Dinout = '1' THEN
--				BUSWires <= Din;
--			END IF;
--		END IF;
--	END PROCESS;
	-- define the bus

END Behavior;


LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY addsubUnit IS
	PORT (summand0 : IN  STD_LOGIC_VECTOR(8 DOWNTO 0);
			summand1 : IN  STD_LOGIC_VECTOR(8 DOWNTO 0);
			Result 	: OUT STD_LOGIC_VECTOR(8 DOWNTO 0);
			AddSub : IN STD_LOGIC); -- instruction = 1 means add vice versa.
END addsubUnit;

ARCHITECTURE Behavior OF addsubUnit IS
BEGIN
--	Result <= summand0 + summand1 WHEN instruction = '1' ELSE summand0 - summand1;
	PROCESS (AddSub, summand0, summand1)
	BEGIN
        IF AddSub = '0' THEN
            Result <= summand0 + summand1;
        ELSE
            Result <= summand0 - summand1;
        END IF;
   END PROCESS;
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