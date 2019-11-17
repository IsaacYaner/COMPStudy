library verilog;
use verilog.vl_types.all;
entity part2_vlg_check_tst is
    port(
        Addr            : in     vl_logic_vector(4 downto 0);
        Done            : in     vl_logic;
        Dref            : in     vl_logic_vector(7 downto 0);
        Dtar            : in     vl_logic_vector(7 downto 0);
        Found           : in     vl_logic;
        sampler_rx      : in     vl_logic
    );
end part2_vlg_check_tst;
