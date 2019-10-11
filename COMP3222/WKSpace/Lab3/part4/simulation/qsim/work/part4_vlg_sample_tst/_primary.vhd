library verilog;
use verilog.vl_types.all;
entity part4_vlg_sample_tst is
    port(
        Clk             : in     vl_logic;
        D               : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end part4_vlg_sample_tst;
