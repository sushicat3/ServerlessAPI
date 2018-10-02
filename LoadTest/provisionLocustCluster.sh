peg up master.yml
peg up workers.yml
peg fetch locust-cluster
# note ip of master node
peg scp to-rem locust-cluster 1 locustfile.py .
peg scp to-rem locust-cluster 2 locustfile.py .
peg scp to-rem locust-cluster 3 locustfile.py .
peg scp to-rem locust-cluster 4 locustfile.py .
peg scp to-rem locust-cluster 5 locustfile.py .
peg scp to-rem locust-cluster 6 locustfile.py .