library verilog;
use verilog.vl_types.all;
entity part3_vlg_check_tst is
    port(
        REDG            : in     vl_logic_vector(1 downto 0);
        REDR            : in     vl_logic_vector(9 downto 0);
        sampler_rx      : in     vl_logic
    );
end part3_vlg_check_tst;
