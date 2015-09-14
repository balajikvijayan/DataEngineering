# We use the CentOS version 7 as a base for our own image that is described by this file.
FROM centos:7
MAINTAINER Galvanize

RUN echo "Expose SSH port"
EXPOSE 22 

RUN echo "Install openssh"
RUN yum -y install openssl openssh-server passwd shadow-utils sudo && yum clean all

RUN echo "Install basic packages"
RUN yum -y install vim nano wget 

RUN echo "Configure root Account"
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd

RUN echo "SSH login fix for Docker"
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config

RUN echo "Setup gstudent user with sudo-rights (no password needed)"
RUN useradd -m -d /home/gstudent -s /bin/bash -c "gstudent user" -p $(openssl passwd -1 gstudent)  gstudent
RUN echo "gstudent ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
#RUN echo "root ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# allow user to login as sudo with no pwd needed for anything
RUN echo "Sets up public keys for ssh for gstudent user.  Assumes your public keys are stored in ./tmp"
RUN mkdir -p /home/gstudent/.ssh
RUN chown -R gstudent:gstudent /home/gstudent/.ssh
RUN chmod 700 /home/gstudent/.ssh
ADD tmp/authorized_keys /home/gstudent/.ssh/authorized_keys
RUN chmod 644 /home/gstudent/.ssh/authorized_keys

# extract this -- do using Ansible
#RUN wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
#RUN bash Miniconda-latest-Linux-x86_64.sh

RUN ssh-keygen -A
RUN echo "Start sshd service"
CMD ["/usr/sbin/sshd", "-D"]