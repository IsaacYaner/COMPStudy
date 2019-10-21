library verilog;
use verilog.vl_types.all;
entity part1 is
    port(
        KEY             : in     vl_logic_vector(0 downto 0);
        SW              : in     vl_logic_vector(1 downto 0);
        HEX1            : out    vl_logic_vector(6 downto 0);
        HEX0            : out    vl_logic_vector(6 downto 0)
    );
end part1;
