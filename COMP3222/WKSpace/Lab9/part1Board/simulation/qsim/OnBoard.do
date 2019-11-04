onerror {quit -f}
vlib work
vlog -work work OnBoard.vo
vlog -work work OnBoard.vt
vsim -novopt -c -t 1ps -L cycloneii_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.OnBoard_vlg_vec_tst
vcd file -direction OnBoard.msim.vcd
vcd add -internal OnBoard_vlg_vec_tst/*
vcd add -internal OnBoard_vlg_vec_tst/i1/*
add wave /*
run -all
