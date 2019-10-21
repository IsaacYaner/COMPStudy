library verilog;
use verilog.vl_types.all;
entity part2_vlg_check_tst is
    port(
        Cout            : in     vl_logic_vector(15 downto 0);
        sampler_rx      : in     vl_logic
    );
end part2_vlg_check_tst;
