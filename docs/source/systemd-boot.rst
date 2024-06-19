Systemd-boot Installation
=========================

Requirements:
-------------

- Secure boot disabled

https://kowalski7cc.xyz/blog/systemd-boot-fedora-32/

Showing Windows entry from another drive while dual-booting
-----------------------------------------------------------

1. **Mount the Windows EFI partition:**

    - Run `sudo fdisk -l` to list partitions.
    - Look for a partition on drive where windows is installed with a size of 100M and type "EFI System".
    - Create a directory and mount the Windows EFI partition that was identified earlier into it:

    .. code-block:: shell
     
        sudo mkdir /mnt/winefi
        sudo mount /dev/nvme0n1p2 /mnt/winefi

3. **Copy the boot configuration data (BCD) to the systemd-boot EFI menu:**

    .. code-block:: shell
   
        sudo cp -R /mnt/winefi/EFI/Microsoft/ /boot/efi/EFI/Microsoft

4. **Unmount the Windows partition and clean up:**

    .. code-block:: shell
   
        sudo umount /mnt/winefi
        sudo rm -rf /mnt/winefi
