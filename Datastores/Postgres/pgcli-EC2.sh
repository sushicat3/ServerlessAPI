sudo yum install python3
sudo yum install gcc
sudo yum install gcc-c++
sudo yum install python3-devel
sudo pip3 install pgcli

# RESOURCES:
# https://amalgjose.com/tag/gcc-failed-with-exit-status-1/

pgcli -h musicbrainz.cw2va02rdk2z.us-east-1.rds.amazonaws.com -U musicbrainz

# copy files from local to EC2
# scp -i "swetal-IAM-keypair.pem" -r ec2-user@ec2-user@ec2-34-238-117-20.compute-1.amazonaws.com City_Of_Somerville_Weekly_Payroll_Gross_Wages_Over_50K_2016.csv