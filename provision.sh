#!/bin/bash

if [[ $EUID -ne 0 ]]
then
  echo "You must run this as root" 2>&1
  exit 1
fi

apt-get update


# basics
apt-get -y install build-essential git unzip make

# python stuff
apt-get install -y python-dev python-virtualenv python-pip
pip install --upgrade pip==1.5.4 wheel==0.22.0 setuptools==2.2

# Oracle Java 7
apt-get -y install python-software-properties
add-apt-repository -y ppa:webupd8team/java
apt-get -y update
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
apt-get -y install oracle-java7-installer oracle-java7-set-default

# leiningen
wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein -O /usr/local/bin/lein
chmod +x /usr/local/bin/lein
chown vagrant /usr/local/bin/lein
lein

# streamparse
pip install streamparse
