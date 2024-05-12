Systemd-boot Installation
=========================

Requirements:
-------------

- Secure boot disabled
- Running EFI (check with: ``test -d /sys/firmware/efi && echo EFI || echo Legacy``)

Installation Steps
------------------

1. Create a folder in the ESP directory with the machine-id in the name:

    .. code-block:: shell

        sudo mkdir /boot/efi/$(cat /etc/machine-id)

2. Remove GRUB from DNF's protected packages:

    .. code-block:: shell

        sudo rm /etc/dnf/protected.d/{grub,shim}*

3. Install systemd-boot and then uninstall GRUB related packages:

    .. code-block:: shell

        sudo dnf remove -y grubby grub2\* memtest86\*
        sudo dnf install -y systemd-boot-unsigned sdubby

4. Install the bootloader and the kernel entries:

    .. code-block:: shell

        cat /proc/cmdline | cut -d ' ' -f 2- | sudo tee /etc/kernel/cmdline
        sudo bootctl install
        sudo kernel-install add $(uname -r) /lib/modules/$(uname -r)/vmlinuz
        sudo dnf reinstall kernel-core

Verification
------------

You can verify everything is working correctly with:

.. code-block:: shell

    sudo bootctl

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
   
        sudo cp -R /mnt/winefi/EFI/Microsoft/ /boot/efi/Microsoft

4. **Unmount the Windows partition and clean up:**

    .. code-block:: shell
   
        sudo umount /mnt/winefi
        sudo rm -rf /mnt/winefi
