library verilog;
use verilog.vl_types.all;
entity part2 is
    port(
        MClock          : in     vl_logic;
        PClock          : in     vl_logic;
        Resetn          : in     vl_logic;
        Run             : in     vl_logic;
        BUSWires        : out    vl_logic_vector(8 downto 0);
        Done            : out    vl_logic
    );
end part2;
