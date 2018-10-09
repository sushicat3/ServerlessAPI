# ---------------------------------------------------------------------
# commands for provisioning the locust cluster
# ---------------------------------------------------------------------
# 		- use master and workers yaml template files to provision cluster
# 		- fetch the hostnames and ips and store locally
# 		- copy the locustfile to each node in the cluster

peg up master.yml
peg up workers.yml
peg fetch locust-cluster
peg scp to-rem locust-cluster 1 locustfile.py .
peg scp to-rem locust-cluster 2 locustfile.py .
peg scp to-rem locust-cluster 3 locustfile.py .
peg scp to-rem locust-cluster 4 locustfile.py .
peg scp to-rem locust-cluster 5 locustfile.py .
peg scp to-rem locust-cluster 6 locustfile.py .
# ...
# peg scp to-rem locust-cluster <n> locustfile.py .
