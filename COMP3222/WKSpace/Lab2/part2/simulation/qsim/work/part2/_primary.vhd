library verilog;
use verilog.vl_types.all;
entity part2 is
    port(
        SW              : in     vl_logic_vector(3 downto 0);
        HEX0            : out    vl_logic_vector(6 downto 0);
        HEX1            : out    vl_logic_vector(6 downto 0);
        mm              : out    vl_logic_vector(3 downto 0)
    );
end part2;
