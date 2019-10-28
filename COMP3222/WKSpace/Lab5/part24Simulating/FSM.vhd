LIBRARY ieee; 
USE ieee.std_logic_1164.all;
USE ieee.std_logic_unsigned.all;

ENTITY FSM IS 
	PORT (w, CLK, reset	: IN	STD_LOGIC;
			z					: OUT	STD_LOGiC;
			stateOut			: OUT STD_LOGIC_VECTOR(3 DOWNTO 0)); 
END FSM;



ARCHITECTURE Behavior OF FSM IS 

	TYPE State_type IS (A, B, C, D, E, F, G, H, I);
	attribute syn_encoding : string; 
	attribute syn_encoding of State_type : type is "0000 0001 0010 0011 0100 0101 0110 0111 1000";
 
	SIGNAL state, nextState : State_type; -- y_Q is present state, y_D is next state 

BEGIN 
 
	PROCESS(w, state)
	BEGIN 
		CASE state IS 				--Due to error without comply of the design.... sign
			WHEN A =>
				IF (w = '0') THEN
					nextState <= B; 
				ELSE 
					nextState <= F; 
				END IF; 
				
			WHEN B =>
				IF (w = '0') THEN
					nextState <= C;
				ELSE
					nextState <= F;
				END IF;
				
			WHEN C =>
				IF (w = '0') THEN
					nextState <= D;
				ELSE
					nextState <= F;
				END IF;
				
			WHEN D =>
				IF (w = '0') THEN
					nextState <= E;
				ELSE
					nextState <= F;
				END IF;
				
			WHEN E =>
				IF (w = '0') THEN
					nextState <= E;
				ELSE
					nextState <= F;
				END IF;
				
			WHEN F =>
				IF	(w = '1') THEN
					nextState <= G;
				ELSE
					nextState <= B;
				END IF;
			WHEN G =>
				IF	(w = '1') THEN
					nextState <= H;
				ELSE
					nextState <= B;
				END IF;
			WHEN H =>
				IF	(w = '1') THEN
					nextState <= I;
				ELSE
					nextState <= B;
				END IF;
			WHEN I =>
				IF (w = '1') THEN
					nextState <= I;
				ELSE
					nextState <= B;
				END IF;
		END CASE; 
	END PROCESS; -- state table
	
	PROCESS (CLK) -- state ﬂip-ﬂops 
	BEGIN
		IF CLK'event AND CLK = '1' THEN
			
			IF reset = '0' THEN
				state <= A;
			ELSE
				state <= nextState;
			END IF;
		END IF;
	END PROCESS;
	
	PROCESS(state)	--out put of LEDR
	BEGIN 
	
		IF (state = E) OR (state = I) THEN
			z <= '1';
		ELSE
			z <= '0';
		END IF;
		CASE state IS 
			WHEN A =>
				stateOut <= "0000"; 
			WHEN B =>
				stateOut <= "0001";
			WHEN C =>
				stateOut <= "0010";
			WHEN D =>
				stateOut <= "0011";
			WHEN E =>
				stateOut <= "0100";
			WHEN F =>
				stateOut <= "0101";
			WHEN G =>
				stateOut <= "0110";
			WHEN H =>
				stateOut <= "0111";
			WHEN I =>
				stateOut <= "1000";
		END CASE; 
	END PROCESS; -- state table
END Behavior;
