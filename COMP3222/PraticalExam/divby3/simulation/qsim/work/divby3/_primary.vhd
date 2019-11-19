library verilog;
use verilog.vl_types.all;
entity divby3 is
    port(
        clk             : in     vl_logic;
        Resetn          : in     vl_logic;
        A               : in     vl_logic_vector(7 downto 0);
        s               : in     vl_logic;
        R               : out    vl_logic_vector(7 downto 0);
        Div3            : out    vl_logic;
        Done            : out    vl_logic
    );
end divby3;
