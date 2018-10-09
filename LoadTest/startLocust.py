import subprocess
import sys


# ---------------------------------------------------------------------
# get optional command line argument: api url to load test
# ---------------------------------------------------------------------
if len(sys.argv) == 1:
	api_endpoint = 'https://vrhgkesjbg.execute-api.us-east-1.amazonaws.com/prod'
elif len(sys.argv) == 2:
	api_endpoint == sys.argv[1]
else:
	print('usage: python3 startLocust.py <optional-api-endpoint-url>')
	sys.exit()


# ---------------------------------------------------------------------
# get the master ip and number of nodes in the cluster
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

def getMasterIP(description):
	lines = description.split('\n')
	for line in lines:
		if 'Hostname' in line:
			ipidx = line.find('ip') + 3
			ip = line[ipidx:].replace('-', '.')
			return ip

numNodes = getNumNodes(peg_out)
master_ip = getMasterIP(peg_out)

# print(str(numNodes))
# print(master_ip)


# ---------------------------------------------------------------------
# start running a distributed locust cluster
# ---------------------------------------------------------------------
locust_m_cmd = '/home/ubuntu/.local/bin/locust --host=' + api_endpoint + ' --master'
locust_s_cmd = '/home/ubuntu/.local/bin/locust --host=' + api_endpoint + ' --slave --master-host=' + master_ip

# run the master node
m_command = 'peg sshcmd-node locust-cluster ' + str(1) + ' "' + locust_m_cmd + '" &'
m_command_proc = subprocess.run([m_command], shell=True)

# run the worker nodes
for x in range(2, numNodes+1):
	s_command = 'peg sshcmd-node locust-cluster ' + str(x) + ' "' + locust_s_cmd + '" &'
	s_command_proc = subprocess.run([s_command], shell=True)