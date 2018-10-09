import subprocess


# ---------------------------------------------------------------------
# get the number of nodes in the cluster
# ---------------------------------------------------------------------
peg_proc = subprocess.run(['peg describe locust-cluster'], shell=True, stdout=subprocess.PIPE)
peg_out = peg_proc.stdout.decode()

def getNumNodes(description):
	lines = description.split('\n')
	line_count = 0
	for line in lines:
		if line_count == 1:
			return int(line.strip().split()[0])
		line_count = line_count+1

numNodes = getNumNodes(peg_out)


# ---------------------------------------------------------------------
# stop locust in every node on the cluster
# ---------------------------------------------------------------------
for x in range(1, numNodes+1):
	locust_stop = 'peg sshcmd-node locust-cluster ' + str(x) + ' "killall -9 locust"'
	locust_stop_proc = subprocess.run([locust_stop], shell=True)


# ---------------------------------------------------------------------
# commands to clean up peg processes on your machine
# ---------------------------------------------------------------------
# ps aux | grep locust | awk '{print "kill -9 "$2}'
# ps aux | grep locust | awk '{print "kill -9 "$2}' | bash
# ps aux | grep locust 