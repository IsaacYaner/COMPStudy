library verilog;
use verilog.vl_types.all;
entity syncnt8 is
    port(
        Enable          : in     vl_logic;
        Clock           : in     vl_logic;
        Clear           : in     vl_logic;
        Cout            : out    vl_logic_vector(7 downto 0)
    );
end syncnt8;
