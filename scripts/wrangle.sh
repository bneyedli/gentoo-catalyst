#!/bin/bash

useradd bnadmin
gpasswd -a bnadmin wheel
echo "root:$(pwgen -s -1 50)" | chpasswd --md5 root
echo "bnadmin:$(pwgen -s -1 50)" | chpasswd --md5 root
