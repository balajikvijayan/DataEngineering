#!/usr/bin/env bash

cp /vagrant/hosts /etc/hosts
cp /vagrant/resolv.conf /etc/resolv.conf

sudo su -
yum install ntp -y
service ntpd start
#service iptables stop
systemctl stop firewalld


mkdir -p /root/.ssh; chmod 700 /root/.ssh
cp /vagrant/id_rsa /root/.ssh
cp /vagrant/id_rsa.pub /root/.ssh
touch /root/.ssh/authorized_keys; chmod 640 /root/.ssh/authorized_keys
cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys

echo "if test -f /sys/kernel/mm/redhat_transparent_hugepage/defrag; then echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag fi" >> /etc/rc.local

#/etc/init.d/iptables stop

# Increasing swap space
sudo dd if=/dev/zero of=/swapfile bs=1024 count=1024k
sudo mkswap /swapfile
sudo swapon /swapfile
echo "/swapfile       none    swap    sw      0       0" >> /etc/fstab

#sudo yum upgrade -y
