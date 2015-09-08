#!/usr/bin/env bash

sudo su -
cd /etc/yum.repos.d/
wget http://s3.amazonaws.com/dev.hortonworks.com/ambari/centos7/2.x/BUILDS/2.1.0-1409/ambaribn.repo
yum install ambari-server -y
ambari-server setup -s
ambari-server start
cp /etc/yum.repos.d/ambaribn.repo /etc/yum.repos.d/ambari.repo

