subarch: amd64
version_stamp: 2015.12
target: livecd-stage2
rel_type: hardened
profile: hardened/linux/amd64
snapshot: 2015.12.17
source_subpath: hardened/livecd-stage1-amd64-2015.12

livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/fsscript: /var/data/catalyst/release/releng/releases/weekly/scripts/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --oldconfig --makeopts=-j5
livecd/iso: livecd-amd64-hardened-installer-latest.iso
livecd/type: gentoo-release-minimal

livecd/volid: Gentoo Linux latest amd64 LiveCD

livecd/overlay: /var/data/catalyst/release/releng/releases/weekly/overlays/common/overlay/livecd
livecd/root_overlay: /var/data/catalyst/release/releng/releases/weekly/overlays/common/root_overlay

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources bc
boot/kernel/gentoo/config: /var/data/catalyst/release/releng/releases/weekly/kconfig/amd64/livecd-2.6.24.config
boot/kernel/gentoo/use: atm usb

livecd/empty:
	/var/tmp
	/var/empty
	/var/run
	/var/state
	/var/cache/edb/dep
	/tmp
	/usr/portage
	/usr/src
	/root/.ccache
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
