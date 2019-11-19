library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;


entity onboardTest is
    Port(SW		:	IN STD_LOGIC_VECTOR(9 DOWNTO 0);
			KEY	:	IN STD_LOGIC_VECTOR(3 DOWNTO 0);
			LEDR	:	OUT STD_LOGIC_VECTOR(7 DOWNTO 0);
			LEDG	:	OUT STD_LOGIC_VECTOR(7 DOWNTO 0));
end onboardTest;

architecture behavioural of onboardTest is

COMPONENT divby3 is
    Port (	clk 		: in  STD_LOGIC;     -- use manual clock
			Resetn 		: in  STD_LOGIC;
			A			: in  STD_LOGIC_VECTOR(7 downto 0);
			s			: in  STD_LOGIC;
			R			: out STD_LOGIC_VECTOR(7 downto 0);
			Div3		: out STD_LOGIC;
			Done		: out STD_LOGIC);
END COMPONENT;

begin
	
	divideby3 : divby3 PORT MAP (KEY(3), KEY(0), SW(7 DOWNTO 0), SW(9), LEDR(7 DOWNTO 0), LEDG(7), LEDG(0));
	
end behavioural;