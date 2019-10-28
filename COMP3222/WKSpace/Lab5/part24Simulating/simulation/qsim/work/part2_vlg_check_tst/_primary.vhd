library verilog;
use verilog.vl_types.all;
entity part2_vlg_check_tst is
    port(
        LEDG            : in     vl_logic_vector(0 downto 0);
        LEDR            : in     vl_logic_vector(3 downto 0);
        sampler_rx      : in     vl_logic
    );
end part2_vlg_check_tst;
