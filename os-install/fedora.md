#fedora iso 镜像刻录
sudo dd bs=4M count=512 if=~/data/Fedora-Workstation-Live-x86_64-27-1.6.iso of=/dev/sdb1 && sync
```
set root=(hd0,msdos)
linuxefi (hd0,msdos)/isolinux/vmlinuz
initrdefi (hd0, msdos)/isolinux/initrd
boot
```

```
fdisk -l
mkfs.vfat /dev/sdb1   #/dev/sdb1 是u盘
```

查看所有的磁盘类型:
```
lsblk -f
```

```
sudo file -s /dev/sdc1
```
