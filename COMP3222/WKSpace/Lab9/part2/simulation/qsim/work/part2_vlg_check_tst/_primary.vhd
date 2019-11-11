library verilog;
use verilog.vl_types.all;
entity part2_vlg_check_tst is
    port(
        BUSWires        : in     vl_logic_vector(8 downto 0);
        Done            : in     vl_logic;
        sampler_rx      : in     vl_logic
    );
end part2_vlg_check_tst;
