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

.. autosummary::
   :toctree: generated

   lumache
