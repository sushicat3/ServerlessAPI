# for lambda (non-distributed)
locust --host=https://lvtr06hwf0.execute-api.us-east-1.amazonaws.com/prod

# for lambda (distributed)
locust --host=https://lvtr06hwf0.execute-api.us-east-1.amazonaws.com/prod --master
locust --host=https://lvtr06hwf0.execute-api.us-east-1.amazonaws.com/prod --slave --master-host=35.174.223.10 # public ip
locust --host=https://lvtr06hwf0.execute-api.us-east-1.amazonaws.com/prod --slave --master-host=10.0.0.8 # private ip

# for ec2 (distributed)
locust --host=http://ec2-54-156-249-48.compute-1.amazonaws.com --master
locust --host=http://ec2-54-156-249-48.compute-1.amazonaws.com --slave --master-host=35.174.223.10
