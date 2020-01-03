LIBRARY ieee ;
use ieee.numeric_std.all;
USE ieee.std_logic_1164.all ;
USE ieee.std_logic_unsigned.all ;

ENTITY part2 IS
	PORT(	Clock, Resetn	: IN STD_LOGIC ;
			s					: IN STD_LOGIC ;
			Data 				: IN STD_LOGIC_VECTOR(7 DOWNTO 0) ;
			Dtar				: OUT STD_LOGIC_VECTOR(7 DOWNTO 0);
			Dref				: OUT STD_LOGIC_VECTOR(7 DOWNTO 0);
			DL				: OUT STD_LOGIC_VECTOR(4 DOWNTO 0);
			DR				: OUT STD_LOGIC_VECTOR(4 DOWNTO 0);
			Dsth			: OUT STD_LOGIC_VECTOR(7 DOWNTO 0);
			Addr 				: OUT STD_LOGIC_VECTOR(4 DOWNTO 0) ;
			Found				: OUT STD_LOGIC ;
			Done 				: OUT STD_LOGIC ) ;
END part2 ;

ARCHITECTURE Behavior OF part2 IS
	COMPONENT memory_block IS -- model used latches address and data internally, hence 2-cycle delay
		PORT(	address	: IN STD_LOGIC_VECTOR (4 DOWNTO 0);
				clock		: IN STD_LOGIC ;
				data		: IN STD_LOGIC_VECTOR (7 DOWNTO 0);
				wren		: IN STD_LOGIC ;
				q			: OUT STD_LOGIC_VECTOR (7 DOWNTO 0));
	END COMPONENT;
	COMPONENT regne IS
		GENERIC ( N : INTEGER := 8 ) ;
		PORT(	D 			: IN 		STD_LOGIC_VECTOR(N-1 DOWNTO 0) ;
				E		 	: IN 		STD_LOGIC ;
				Resetn	: IN		STD_LOGIC;
				Clock 	: IN 		STD_LOGIC ;
				Q 			: OUT 	STD_LOGIC_VECTOR(N-1 DOWNTO 0) ) ;
	END COMPONENT;
	
	-- any other components
	
	TYPE State_type IS (SI, S1, S2, S3, S4, S5, S6); -- your states
	SIGNAL y, y_next : State_type ;
	
	SIGNAL LD, iniLR, LR, MR, ML, Finish : STD_LOGIC;-- your signals
	SIGNAL sum : UNSIGNED(4 DOWNTO 0);
	SIGNAL L, R, M : STD_LOGIC_VECTOR(4 DOWNTO 0);
	SIGNAL ref, tar, memval : STD_LOGIC_VECTOR(7 DOWNTO 0);
BEGIN

	Dtar <= tar;	
	Dref <= ref;
	DL <= L;
	DR <= R;
	Dsth <= memval;

	statetable : PROCESS(Resetn, Finish, ref, tar, y, s)
	BEGIN
		IF Resetn = '0' THEN
			y_next <= SI;
		ELSE
			CASE y IS
				WHEN SI => 
					IF s = '1' THEN
						y_next <= S1;
					ELSE 
						y_next <= SI;
					END IF;
				WHEN S1 =>
					y_next <= S2;
				WHEN S2 =>
					y_next <= S3;
				WHEN S3 =>
					y_next <= S4;
				WHEN S4 =>
					IF (ref > tar) OR (ref < tar) THEN
						IF Finish = '1' THEN
							y_next <= S5;
						ELSE 
							y_next <= S1;
						END IF;
					ELSE 
						y_next <= S6;
					END IF;
				WHEN S5 =>
					IF s = '1' THEN
						y_next <= S5;
					ELSE
						y_next <= SI;
					END IF;
				WHEN S6 =>
					IF s = '1' THEN
						y_next <= S6;
					ELSE
						y_next <= SI;
					END IF;
			END CASE;
		END IF;
	END PROCESS;
	
	fsmflipflops : PROCESS(Resetn, Clock)
	BEGIN
		IF Resetn = '0' THEN
			y <= SI;
		ELSIF Clock'event AND Clock = '1' THEN
			y <= y_next;
		END IF;
	END PROCESS;	
	
	controlsignals : PROCESS(Resetn, y, ref, tar, M)
	BEGIN
		LD <= '0'; iniLR <= '0'; LR <= '0'; MR <= '0'; Addr <= "00000";
		ML <= '0'; Done <= '0'; Found <= '0';
		IF Resetn = '0' THEN
			null;
		ELSE
			CASE y IS
				WHEN SI =>
					LD <= '1';
					iniLR <= '1';
				WHEN S1 =>
					IF L = R OR L > R THEN 
						Finish <= '1';
					ELSE 
						Finish <= '0';
					END IF;
				WHEN S2 =>
					null;
				WHEN S3 =>
					LR <= '1';
					null;
				WHEN S4 =>
					IF ref > tar THEN
						MR <= '1';
					ELSIF ref < tar THEN
						ML <= '1';
					END IF;
				WHEN S5 =>
					Done <= '1';
				WHEN S6 =>
					Done <= '1';
					Found <= '1';
					Addr <= M;
			END CASE;
		END IF;
	END PROCESS;
	
	fsmdata : PROCESS(Clock)
	BEGIN 
		IF iniLR = '1' THEN
			L <= "00000";
			R <= "11111";
		END IF;
		IF LR = '1' THEN
			ref <= memval;
		END IF;
		IF MR = '1' THEN
			R <= M-1;
		END IF;
		IF ML = '1' THEN
			L <= M+1;
		END IF;
		IF Clock'event AND Clock = '1' THEN		
			M <= STD_LOGIC_VECTOR(sum srl 1);
		END IF;
	END PROCESS;
	
	sum <= unsigned(L + R);
	
	readMemory: memory_block PORT MAP (M, Clock, "00000000", '0', memval);
	
	LoadData : regne PORT MAP (Data, LD, Resetn, Clock, tar);
	
END Behavior ;

LIBRARY ieee ;
USE ieee.std_logic_1164.all ;

-- n-bit register with synchronous reset and enable
ENTITY regne IS
	GENERIC ( N : INTEGER := 8 ) ;
	PORT(	D 			: IN 		STD_LOGIC_VECTOR(N-1 DOWNTO 0) ;
			E		 	: IN 		STD_LOGIC ;
			Resetn	: IN		STD_LOGIC;
			Clock 	: IN 		STD_LOGIC ;
			Q 			: OUT 	STD_LOGIC_VECTOR(N-1 DOWNTO 0) ) ;
END regne ;

ARCHITECTURE Behavior OF regne IS
BEGIN
	PROCESS
	BEGIN
		WAIT UNTIL (Clock'EVENT AND Clock = '1') ;
		IF (Resetn = '0') THEN
			Q <= (OTHERS => '0');
		ELSIF (E = '1') THEN
			Q <= D;
		END IF ;
	END PROCESS ;
END Behavior ;