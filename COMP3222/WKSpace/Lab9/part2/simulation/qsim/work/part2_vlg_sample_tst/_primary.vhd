library verilog;
use verilog.vl_types.all;
entity part2_vlg_sample_tst is
    port(
        MClock          : in     vl_logic;
        PClock          : in     vl_logic;
        Resetn          : in     vl_logic;
        Run             : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end part2_vlg_sample_tst;
