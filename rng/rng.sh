#! /bin/bash

# Run ngrep on a remote system, download the resulting pcap and analyze
# it in wireshark.
# Author: Lorenzo Cabrini <lorenzo.cabrini@gmail.com>

host=$1
remote=$2
tm=$3
pcap=$4

if [[ -z $host ]]; then
    echo "E: no host specified"
    exit 1
fi

if [[ -z $remote ]]; then
    echo "E: no remote server specified"
    exit 1
fi

if [[ -n $pcap ]]; then
    pcap=$pcap-$(date +"%Y%m%d%H%M").pcap
else
    pcap=pcap-$(date +"%Y%m%d%H%M").pcap
fi

if [[ -z $tm ]]; then
    tm=10s
fi

cmd="timeout $tm ngrep -W byline -d any udp and port 5060 and host $host -O $pcap"
ssh root@$remote $cmd 
sftp -b /dev/stdin root@$remote <<EOF
get $pcap
EOF

ssh root@$remote rm $pcap 

which wireshark > /dev/null 2>&1
r=$?
if [[ $r -ne 0 ]]; then
    echo "Wireshark is not installed. Trying to install it"
    for pm in dnf yum apt; do
        $pm --version > /dev/null 2>&1
        r2=$?
        if [[ $r2 -eq 0 ]]; then
            sudo $pm install wireshark
            break
        fi
    done
fi

wireshark $pcap
