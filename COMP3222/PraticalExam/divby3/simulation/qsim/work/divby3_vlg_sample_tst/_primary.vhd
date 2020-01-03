library verilog;
use verilog.vl_types.all;
entity divby3_vlg_sample_tst is
    port(
        A               : in     vl_logic_vector(7 downto 0);
        clk             : in     vl_logic;
        Resetn          : in     vl_logic;
        s               : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end divby3_vlg_sample_tst;
