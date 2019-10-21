library verilog;
use verilog.vl_types.all;
entity syncnt8_vlg_sample_tst is
    port(
        Clear           : in     vl_logic;
        Clock           : in     vl_logic;
        Enable          : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end syncnt8_vlg_sample_tst;
