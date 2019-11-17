LIBRARY ieee ;
USE ieee.std_logic_1164.all ;
use ieee.numeric_std.all;
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
	
	TYPE State_type IS (SI, S1, S2, S3, S4, S5, S7); -- your states
	SIGNAL y, y_next : State_type ;
	
	SIGNAL LD, CA, LR, Finish : STD_LOGIC;
	SIGNAL sum : UNSIGNED(4 DOWNTO 0);
	SIGNAL L, R, M : STD_LOGIC_VECTOR(4 DOWNTO 0);-- your signals
	SIGNAL ref, tar, sth: STD_LOGIC_VECTOR(7 DOWNTO 0);
BEGIN
	
	Dtar <= tar;
	Dref <= ref;
	DL <= L;
	DR <= R;
	Dsth <= sth;
	
	statetable : PROCESS(Resetn)
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
					IF L > R THEN
						y_next <= S4;
					ELSE 
						y_next <= S7;
					END IF;
				WHEN S7 =>
					y_next <= S2;
				WHEN S2 =>
					y_next <= S3;
				WHEN S6 =>
					y_next <= S3;
				WHEN S3 =>
					IF (ref > tar) OR (ref < tar) THEN
						IF Finish = '1' THEN
							y_next <= S4;
						ELSE
							y_next <= S1;
						END IF;
					ELSE
						y_next <= S5;
					END IF;
				WHEN S4 =>
					IF s = '0' THEN
						y_next <= SI;
					ELSE
						y_next <= S4;
					END IF;
				WHEN S5 =>
					IF s = '0' THEN
						y_next <= SI;
					ELSE
						y_next <= S5;
					END IF;
				WHEN others =>
					null;
			END CASE;
		END IF;
	END PROCESS;
	
	
	fsmflipflops : PROCESS(Clock, Resetn)
	BEGIN
		IF Resetn = '0' THEN
			y <= SI;
		ELSIF Clock'event AND Clock = '1' THEN
			y <= y_next;
		END IF;
	END PROCESS;
	
	
	Addr <= M;
	FSM_outputs : PROCESS(y, s)
	BEGIN
		LD <= '0'; LR <= '0'; Done <= '0';Finish <= '0';
			CASE y IS
				WHEN SI =>
					ref <= (others => '0');
					L <= "00000";
					R <= "11111";
					Found <= '0';
					IF s = '0' THEN
						LD <= '1';
					END IF;
				WHEN S1 =>
					LR <= '1';
					IF L = R THEN
						Finish <= '1';
					ELSE
						Finish <= '0';
					END IF;
				
				WHEN S2 =>
					ref <= sth;		
			
				WHEN S6 =>
					null;
					
				WHEN S3 =>
					IF ref > tar THEN
						R <= M - 1;
					ELSIF ref < tar THEN
						L <= M + 1;
					END IF;
					
				WHEN S4 =>
					Done <= '1';
					
				WHEN S5 =>
					Done <= '1';
					Found <= '1';
					--Addr <= M;
					
				WHEN others =>
					null;
			END CASE;
	END PROCESS;
	
	middlepoint : PROCESS(Clock, L, R)
	BEGIN	
		sum <= unsigned(L + R);
		IF Clock'event AND Clock = '1' THEN
			M <= STD_LOGIC_VECTOR(sum srl 1);
		END IF;
	END PROCESS;
	
	loadReferent : memory_block PORT MAP (M, Clock, "00000000", '0', sth);
	
	LoadData : regne PORT MAP (Data, '1', Resetn, Clock, tar);
	-- your code

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