library verilog;
use verilog.vl_types.all;
entity part2_vlg_sample_tst is
    port(
        Clock           : in     vl_logic;
        Data            : in     vl_logic_vector(7 downto 0);
        Resetn          : in     vl_logic;
        s               : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end part2_vlg_sample_tst;
