onerror {quit -f}
vlib work
vlog -work work syncnt8.vo
vlog -work work syncnt8.vt
vsim -novopt -c -t 1ps -L cycloneii_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.syncnt8_vlg_vec_tst
vcd file -direction syncnt8.msim.vcd
vcd add -internal syncnt8_vlg_vec_tst/*
vcd add -internal syncnt8_vlg_vec_tst/i1/*
add wave /*
run -all
