# script for setting up Locust on EC2s

# need pip3 on EC2 to install locustio for python3
# get pip3
# install pip 3
# update the profile script with the local path (profile script will be one of .profile, .bash_profile, or .bash_login, in this case it is .profile)
# source the profile script
# now that pip3 works install locust

curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
# ls -a ~
echo "export PATH=~/.local/bin:$PATH" >> .profile
source ~/.profile
# pip -V
python3 -m pip install locustio --user
# locust -V


