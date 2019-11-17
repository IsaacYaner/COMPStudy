library verilog;
use verilog.vl_types.all;
entity part2 is
    port(
        Clock           : in     vl_logic;
        Resetn          : in     vl_logic;
        s               : in     vl_logic;
        Data            : in     vl_logic_vector(7 downto 0);
        Addr            : out    vl_logic_vector(4 downto 0);
        Dtar            : out    vl_logic_vector(7 downto 0);
        Dref            : out    vl_logic_vector(7 downto 0);
        Found           : out    vl_logic;
        Done            : out    vl_logic
    );
end part2;
