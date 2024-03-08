include "qelib1.inc";

qreg q[4];
creg c[4];
reset q[0];
x q[0];
measure q[0] -> c[0];
