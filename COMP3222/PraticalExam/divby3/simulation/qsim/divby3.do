onerror {quit -f}
vlib work
vlog -work work divby3.vo
vlog -work work divby3.vt
vsim -novopt -c -t 1ps -L cycloneii_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.divby3_vlg_vec_tst
vcd file -direction divby3.msim.vcd
vcd add -internal divby3_vlg_vec_tst/*
vcd add -internal divby3_vlg_vec_tst/i1/*
add wave /*
run -all
