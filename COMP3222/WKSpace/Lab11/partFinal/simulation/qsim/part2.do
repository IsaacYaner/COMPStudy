onerror {quit -f}
vlib work
vlog -work work part2.vo
vlog -work work part2.vt
vsim -novopt -c -t 1ps -L cycloneii_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.part2_vlg_vec_tst
vcd file -direction part2.msim.vcd
vcd add -internal part2_vlg_vec_tst/*
vcd add -internal part2_vlg_vec_tst/i1/*
add wave /*
run -all
