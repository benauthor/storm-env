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
pip install --upgrade pip wheel setuptools ipython ipdb

# Oracle Java 7
apt-get -y install python-software-properties
add-apt-repository -y ppa:webupd8team/java
apt-get -y update
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
apt-get -y install oracle-java7-installer oracle-java7-set-default

# maven
apt-get install maven

# zookeeper (requires java 7)
wget http://www.carfab.com/apachesoftware/zookeeper/stable/zookeeper-3.4.6.tar.gz -O /zookeeper.tar.gz
tar -xzf /zookeeper.tar.gz -C/
mv /zookeeper-3.4.6 /zookeeper
chown -R vagrant /zookeeper

# kafka
wget http://mirrors.advancedhosters.com/apache/kafka/0.9.0.0/kafka_2.11-0.9.0.0.tgz -O /kafka.tar.gz
tar -xzf /kafka.tar.gz -C/
mv /kafka_2.11-0.9.0.0 /kafka
chown -R vagrant /kafka

# librdkafka
apt-get install zlib1g-dev libffi-dev
git clone https://github.com/edenhill/librdkafka.git /opt/librdkafka
chown -R vagrant /opt/librdkafka
cd /opt/librdkafka
./configure
make
sudo make install
# export LD_LIBRARY_PATH=/usr/local/lib

# leiningen
wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein -O /usr/local/bin/lein
chmod +x /usr/local/bin/lein
chown vagrant /usr/local/bin/lein
lein

# supervisor
apt-get -y install supervisor
rm -rf /etc/supervisor/conf.d
ln -s /vagrant/supervisor /etc/supervisor/conf.d
supervisorctl reload

# python packages
pip install -r /vagrant/requirements.txt
