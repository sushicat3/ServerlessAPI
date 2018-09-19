#!/bin/sh

# set up apt repository
# https://wiki.postgresql.org/wiki/Apt
sudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt-get update
sudo apt-get upgrade

# install postgres
sudo apt-get install postgresql-10 postgresql-server-dev-10 postgresql-contrib-10
psql --version

# install git
sudo apt-get install git-core
git --version

# install redis server
sudo apt-get install redis-server
redis-server -v

# install node
sudo apt-get install nodejs
sudo apt-get install nodejs-legacy

# install yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update
sudo apt-get install yarn
yarn --version

# get the key for gpg check
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C777580F


# MASTER NODE:
#     Hostname:   ip-10-0-0-14
#     Public DNS: ec2-18-235-28-19.compute-1.amazonaws.com

# WORKER NODE:
#     Hostname:   ip-10-0-0-10
#     Public DNS: ec2-18-213-200-224.compute-1.amazonaws.com

# WORKER NODE:
#     Hostname:   ip-10-0-0-4
#     Public DNS: ec2-34-192-20-179.compute-1.amazonaws.com

# WORKER NODE:
#     Hostname:   ip-10-0-0-8
#     Public DNS: ec2-18-211-17-185.compute-1.amazonaws.com


# READWRITE => {
#         database    => "musicbrainz_db",
#         username    => "musicbrainz",
#         password        => "musicbrainz",
# #       host            => "",
# #       port            => "",
#     },
