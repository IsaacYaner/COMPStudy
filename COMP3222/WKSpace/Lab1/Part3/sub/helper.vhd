LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY mx21 IS
	PORT (x, y, s	:	IN	 STD_LOGIC;
			m			:	OUT STD_LOGIC);
END mx21;

ARCHITECTURE Behavior OF mx21 IS

BEGIN
	m<=(x and not(s)) or (y and s);
END Behavior;

LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY mx31 IS
	PORT (u, v, w, s0, s1	:	IN	 STD_LOGIC;
			m						:	OUT STD_LOGIC);
END mx31;

ARCHITECTURE Behavior OF mx31 IS

SIGNAL t	:	STD_LOGIC;
BEGIN
	t<=(u and not(s0)) or (v and s0);
	m<=(t and not(s1)) or (w and s1);
END Behavior;