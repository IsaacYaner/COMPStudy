library verilog;
use verilog.vl_types.all;
entity part2_vlg_check_tst is
    port(
        HEX0            : in     vl_logic_vector(6 downto 0);
        HEX1            : in     vl_logic_vector(6 downto 0);
        mm              : in     vl_logic_vector(3 downto 0);
        sampler_rx      : in     vl_logic
    );
end part2_vlg_check_tst;
