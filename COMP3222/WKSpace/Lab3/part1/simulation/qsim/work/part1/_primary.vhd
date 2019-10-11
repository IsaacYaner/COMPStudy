library verilog;
use verilog.vl_types.all;
entity part1 is
    port(
        Clk             : in     vl_logic;
        R               : in     vl_logic;
        S               : in     vl_logic;
        Q               : out    vl_logic
    );
end part1;
