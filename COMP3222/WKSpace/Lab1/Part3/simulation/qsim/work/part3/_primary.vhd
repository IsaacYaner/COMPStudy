library verilog;
use verilog.vl_types.all;
entity part3 is
    port(
        SW              : in     vl_logic_vector(9 downto 0);
        REDR            : out    vl_logic_vector(9 downto 0);
        REDG            : out    vl_logic_vector(1 downto 0)
    );
end part3;
