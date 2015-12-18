subarch: amd64
version_stamp: 2015.12
target: livecd-stage1
rel_type: hardened
profile: hardened/linux/amd64
snapshot: 2015.12.17
source_subpath: hardened-livecd/stage3-amd64-hardened-latest
livecd/use:
	livecd
	loop-aes
	socks5
  -X

livecd/packages:
	app-admin/hddtemp
	app-admin/ide-smart
	app-admin/logrotate
	app-admin/passook
	app-admin/pwgen
	app-admin/sudo
	app-admin/syslog-ng
	app-benchmarks/cpuburn
	app-crypt/gnupg
	app-editors/vim
	app-misc/vlock
  app-misc/tmux
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/ufed
	app-text/wgetpaste
	dev-util/ccache
	dev-vcs/git
  sys-devel/bc
	media-gfx/fbgrab
	net-analyzer/netcat
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/traceroute
  dev-python/boto3
### Masked (no keywords)
	net-firewall/iptables
  net-firewall/ufw
	net-misc/bridge-utils
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/ntp
	net-misc/rdate
	net-misc/vconfig
	net-misc/vpnc
	net-misc/whois
  net-p2p/rtorrent
### Masked (no keywords)
	sys-apps/ethtool
	sys-apps/hdparm
	sys-apps/hwsetup
### Masked (no keywords)
	sys-apps/iproute2
### Masked (no keywords)
	sys-apps/memtester
	sys-apps/netplug
	sys-block/parted
### Masked (no keywords)
	sys-apps/sdparm
	sys-apps/sg3_utils
	sys-apps/mlocate
	sys-apps/smartmontools
	sys-block/disktype
### Masked (-amd64)
	sys-block/partimage
	sys-block/qla-fc-firmware
### Masked (no keywords)
	sys-boot/grub
	sys-boot/syslinux
### Masked (no keywords)
	sys-devel/distcc
### Masked (no keywords)
	sys-fs/cryptsetup
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
### Masked (no keywords)
	sys-fs/lsscsi
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/ntfs3g
	sys-fs/reiserfsprogs
	sys-fs/xfsprogs
	sys-kernel/genkernel
	sys-power/acpid
	sys-process/htop
	sys-process/vixie-cron
	www-client/links
