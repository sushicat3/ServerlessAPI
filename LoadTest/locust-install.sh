# need pip3 on EC2 to install locustio for python3

python3 get-pip.py --user

ls -a ~

# (profile script) one of:
# 	.profile
# 	.bash_profile
# 	.bash_login

nano .profile

# add
# export PATH=~/.local/bin:$PATH
# to bottom of file
# ^O (save), ^X (close)

$ source ~/.profile

pip -V
# pip 18.0 from /home/ubuntu/.local/lib/python3.5/site-packages/pip (python 3.5)

python3 -m pip install locustio --user
locust -V
