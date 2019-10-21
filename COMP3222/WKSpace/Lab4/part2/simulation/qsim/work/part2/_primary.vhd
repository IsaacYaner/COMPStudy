library verilog;
use verilog.vl_types.all;
entity part2 is
    port(
        Enable          : in     vl_logic;
        Cloc            : in     vl_logic;
        Clear           : in     vl_logic;
        Cout            : out    vl_logic_vector(15 downto 0)
    );
end part2;
