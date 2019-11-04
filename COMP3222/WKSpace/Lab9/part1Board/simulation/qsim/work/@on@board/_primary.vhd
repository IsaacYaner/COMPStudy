library verilog;
use verilog.vl_types.all;
entity OnBoard is
    port(
        SW              : in     vl_logic_vector(9 downto 0);
        KEY             : in     vl_logic_vector(1 downto 0);
        LEDR            : out    vl_logic_vector(9 downto 0)
    );
end OnBoard;
