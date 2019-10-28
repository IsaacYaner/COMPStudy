LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY part4 IS
	PORT(	KEY						:IN	std_logic_vector(3 DOWNTO 0);
			SW							:IN	std_logic_vector(9 DOWNTO 0);
			CLOCK_50					:IN	std_logic;
			LEDG						:OUT 	std_logic_vector(0 DOWNTO 0);
			LEDR						:OUT 	std_logic_vector(9 DOWNTO 0));
END part4;

ARCHITECTURE mixed OF part4 IS

	COMPONENT shiftrne IS
		GENERIC ( N : INTEGER := 4 ) ;
		PORT ( R : IN STD_LOGIC_VECTOR(N-1 DOWNTO 0) ;
				 L, E, w : IN STD_LOGIC ;
				 Clock : IN STD_LOGIC ;
	 			 Q : BUFFER STD_LOGIC_VECTOR(N-1 DOWNTO 0) ) ;
	END COMPONENT;
	
	COMPONENT half_sec_timer IS
		PORT ( Clk, Start : IN STD_LOGIC ;
				 TOut : OUT STD_LOGIC);
	END COMPONENT;
	
	SIGNAL Clk, nReset, w, z, shft, TStart, TOut : std_logic;
	SIGNAL LR, CR, QL, QC : std_logic_vector(3 DOWNTO 0); -- length and code values and shift register contents
	SIGNAL sel : std_logic_vector(2 DOWNTO 0);
	TYPE state_t IS (Init); -- add states as required
	SIGNAL y_Q, Y_D : state_t;
	
BEGIN
	Clk <= CLOCK_50;
	nReset <= KEY(0);
	w <= NOT KEY(1); -- start signal
	LEDR(3 DOWNTO 0) <= QC; -- code register
	LEDR(7 DOWNTO 4) <= QL; -- length register
	LEDR(9) <= z; -- Morse output symbol
	sel <= SW(2 DOWNTO 0);
	
	WITH sel SELECT
		CR <= "0010" WHEN "000", -- code register 0=dot, 1=dash, listed from lsb to msb
				"0001" WHEN "001",
				"0101" WHEN "010",
				"0001" WHEN "011",
				"0000" WHEN "100",
				"0100" WHEN "101",
				"0011" WHEN "110",
				"0000" WHEN "111",
				"0000" WHEN OTHERS;
				
	WITH sel SELECT	
		LR <= "0011" WHEN "000", -- length register in unary from lsb
				"1111" WHEN "001",
				"1111" WHEN "010",
				"0111" WHEN "011",
				"0001" WHEN "100",
				"1111" WHEN "101",
				"0111" WHEN "110",
				"1111" WHEN "111",
				"0000" WHEN OTHERS;
	
	LenReg: shiftrne PORT MAP (LR, w, shft, '0', Clk, QL);
	CodeReg: shiftrne PORT MAP (CR, w, shft, '0', Clk, QC);
	Timer: half_sec_timer PORT MAP (Clk, TStart, TOut);
	
	FSM_transitions: PROCESS (y_Q, w, QL(0), QC(0), TOut)
		BEGIN
			CASE y_Q IS
				WHEN Init =>
					Y_D <= Init;
				--
				-- add the next state logic
				--
			END CASE;
		END PROCESS;
		
		FSM_state: PROCESS (Clk, nReset)
			BEGIN
				IF (nReset = '0') THEN
					y_Q <= Init;
				ELSIF (Clk'event AND Clk = '1') THEN
					y_Q <= Y_D;
				END IF;
			END PROCESS;
			
		FSM_outputs: PROCESS (y_Q)
			BEGIN
				shft <= '0'; TStart <= '0'; z <= '0';
				CASE y_Q IS
					WHEN Init =>
						shft <= '1';
					--
					-- add output logic
					--
				END CASE;
			END PROCESS;

END mixed;

LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY shiftrne IS
	GENERIC ( N : INTEGER := 4 ) ;
	PORT ( R : IN STD_LOGIC_VECTOR(N-1 DOWNTO 0) ;
			 L, E, w : IN STD_LOGIC ;
			 Clock : IN STD_LOGIC ;
			 Q : BUFFER STD_LOGIC_VECTOR(N-1 DOWNTO 0) ) ;
END shiftrne ;

ARCHITECTURE Behavior OF shiftrne IS
BEGIN
	PROCESS
	BEGIN
		WAIT UNTIL (Clock'EVENT AND Clock = '1');
		IF (E = '1') THEN -- if enabled
			IF (L = '1') THEN -- depending upon the load signal
				Q <= R; -- either load a new word in parallel
			ELSE 
				Genbits: FOR i IN 0 TO N-2 LOOP -- or shift the word to right
					Q(i) <= Q(i+1);
				END LOOP;
				Q(N-1) <= w;
			END IF;
		END IF;
	END PROCESS;
END Behavior;

LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY half_sec_timer IS
	PORT ( Clk, Start : IN STD_LOGIC ;
			 TOut : OUT STD_LOGIC);
END half_sec_timer;

ARCHITECTURE Behavior OF half_sec_timer IS
	SIGNAL Q : INTEGER RANGE 0 TO 25000000;
BEGIN
	PROCESS (Clk)
	BEGIN
		IF (Clk'event AND Clk = '1') THEN
			IF (Start = '1') THEN
				TOut <= '0';
				Q <= 0;
			ELSIF (Q = 25000000) THEN
				TOut <= '1';
				Q <= 0;
			ELSE
				TOut <= '0';
				Q <= Q + 1;
			END IF;
		END IF;
	END PROCESS;
END Behavior;
