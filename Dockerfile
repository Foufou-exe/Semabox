FROM python:3.11.1

MAINTAINER foufoudu34


# Install dependencies
RUN apt-get update 

RUN apt-get upgrade 

RUN apt-get install -y build-essential libpq-dev rsyslog iputils-ping netbase net-tools openssh-server sudo curl wget git iproute2 systemd systemd-sysv libcurl4-gnutls-dev nmap

# Deplace to /
RUN cd /

# Clone the repository
RUN git clone https://github.com/Foufou-exe/Semabox.git

# Set the working directory to /Semabox
WORKDIR /Semabox

# Install requirements
RUN pip install -r install/requirement.txt


RUN rm -f Semabox.py

# Expose ports
EXPOSE 22
EXPOSE 80

ENTRYPOINT [ "python" , "/Semabox/SemaAPI/API.py" ]



