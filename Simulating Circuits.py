#q1
OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];
reset q[0];
x q[0];
measure q[0] -> c[0];


#q2
OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];
reset q[0];
measure q[0] -> c[0];
x q[0];

#q3

include "qelib1.inc";

qreg q[4];
creg c[4];
reset q[1];
h q[1];
measure q[1] -> c[1];

#4


include "qelib1.inc";

qreg q[4];
creg c[4];
reset q[0];
h q[0];
h q[0];
measure q[0] -> c[0];

