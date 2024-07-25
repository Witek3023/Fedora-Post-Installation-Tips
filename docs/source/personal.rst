Custom Fedora Setup Guide
=========================

Introduction
------------

This guide provides steps to customize your Fedora system for enhanced functionality and performance.

Zsh Installation and Configuration
-----------------------------------

1. Install Zsh:

.. code-block:: shell

    sudo dnf install zsh

2. Change default shell to Zsh:

.. code-block:: shell

    chsh -s $(which zsh)

3. Install Git:

.. code-block:: shell

    sudo dnf install git

4. Install Oh My Zsh:

.. code-block:: shell

    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

5. Configure Zsh by replacing the `.zshrc` file with your custom configuration. You can provide the URL to your `.zshrc` file here.

SELinux Configuration
---------------------

1. Open SELinux configuration file:

.. code-block:: shell

    sudo nano /etc/sysconfig/selinux

2. Disable SELinux by changing the value of `SELINUX` to `disabled`.

3. Check SELinux status:

.. code-block:: shell

    sestatus
             

Custom Kernel
-------------

You can find the custom kernel in the Bieszczaders Kernel-CachyOS repository:

- `Bieszczaders Kernel-CachyOS <https://copr.fedorainfracloud.org/coprs/bieszczaders/kernel-cachyos/>`_

Features

The custom kernel offers the following features:

- **AMD PSTATE Preferred Core**: AMD PSTATE is enabled as default with preferred core.
- **BTRFS and XFS Improvements**: Latest improvements and fixes for BTRFS and XFS filesystems.
- **ZSTD 1.5.5 Patch-Set**: Latest and improved ZSTD 1.5.5 patch-set.
- **UserKSM Daemon**: Integration of UserKSM daemon from pf for memory deduplication.
- **Improved BFQ Scheduler**: Enhanced version of the BFQ scheduler.
- **Linux-Next Patches**: Back-ported patches from linux-next.
- **BBRv3 TCP Congestion Control**: Integration of BBRv3 tcp_congestion_control.
- **Scheduler Patches**: Scheduler patches from linux-next/tip.
- **Improved Sysctl Settings**: General improved sysctl settings and upstream scheduler fixes.
- **OpenRGB and ACS Override Support**: Support for OpenRGB and ACS Override.
- **HDR Patches for AMD GPU's**: HDR patches for AMD GPU's and gamescope.
- **Steam Deck Support**: Default support for Steam Deck.
- **Lenovo Legion Patchset**: Lenovo Legion Patchset (removed from the LTS kernel from version 6.6.30).
- **GitHub copr-linux-cachyos**: Additional patches and enhancements available on GitHub in the copr-linux-cachyos repository.

These features aim to enhance performance, compatibility, and functionality of the kernel for various use cases.
            
1. Enable the Bieszczaders Kernel-CachyOS repository:

.. code-block:: shell

    sudo dnf copr enable bieszczaders/kernel-cachyos

2. Install Kernel-CachyOS and its matched development package:

.. code-block:: shell

    sudo dnf install kernel-cachyos kernel-cachyos-devel-matched

3. Enable the Bieszczaders Kernel-CachyOS Addons repository:

.. code-block:: shell

    sudo dnf copr enable bieszczaders/kernel-cachyos-addons

4. Install required dependencies:

.. code-block:: shell

    sudo dnf install libcap-ng libcap-ng-devel procps-ng procps-ng-devel

5. Install uksmd:

.. code-block:: shell

    sudo dnf install uksmd

6. Enable and start the uksmd service:

.. code-block:: shell

    sudo systemctl enable --now uksmd.service

7. Check uksmd statistics:

.. code-block:: shell

    uksmdstats

Additional Software Installation and Configuration
---------------------------------------------------

1. **Install essential(fully personal) tools:**

   .. code-block:: shell

      sudo dnf install net-tools pip htop neofetch kitty nemo nemo-fileroller nemo-compare nemo-audio-tab nemo-image-converter nemo-pastebin nemo-python nemo-search-helpers git unzip pfetch btop zathura feh pavucontrol ranger vim neovim emacs figlet lolcat perl-Archive-Extract-lzma-IO-Uncompress-UnLzma tar xz p7zip zip gzip cpio unace network-manager-applet blueman libnotify bluez stow sl

2. **Set hardware clock to local time:**

   .. code-block:: shell

        sudo timedatectl set-local-rtc '0'

   Ensures the hardware clock is set to UTC for better time synchronization.

3. **Disable terminal bell**
    .. code-block:: shell

        echo "blacklist pcspkr" | sudo tee /etc/modprobe.d/blacklist-pcspkr.conf > /dev/null

4. **Install Colorscripts**
    .. code-block:: shell
        git clone https://gitlab.com/dwt1/shell-color-scripts.git
        cd shell-color-scripts
        sudo make install

        # Removal
        sudo make uninstall

        # optional for zsh completion
        sudo cp completions/_colorscript /usr/share/zsh/site-functions

Firmware Updates
----------------
   .. code-block:: shell

      sudo fwupdmgr get-devices 
      sudo fwupdmgr refresh --force 
      sudo fwupdmgr get-updates 
      sudo fwupdmgr update

   These commands check for and apply any available firmware updates to ensure your hardware is running the latest firmware.

Power Management Configuration
------------------------------

1. **Install and configure TLP for advanced power management:**

   .. code-block:: shell

      sudo dnf install tlp tlp-rdw

   TLP provides advanced power management features for your Fedora system.

2. **Remove Power Profiles Daemon:**

   .. code-block:: shell

      sudo dnf remove power-profiles-daemon

   TLP and Power Profiles Daemon can conflict, so it's recommended to remove the latter.

3. **Enable TLP service:**

   .. code-block:: shell

      sudo systemctl enable tlp.service

   Ensures TLP starts automatically on boot.

4. **Mask systemd rfkill services:**

   .. code-block:: shell

      sudo systemctl mask systemd-rfkill.service systemd-rfkill.socket

   Prevents conflicts with TLP's radio management.

5. **Add ThinkPad Extras repositories:**

   .. code-block:: shell

      sudo dnf install https://repo.linrunner.de/fedora/tlp/repos/releases/tlp-release.fc$(rpm -E %fedora).noarch.rpm

   These repositories provide additional software packages and updates for TLP.

6. **Install kernel development packages and tp_smapi:**

   .. code-block:: shell

      sudo dnf install kernel-devel akmod-tp_smapi
      sudo dnf --enablerepo=tlp-updates-testing install kernel-devel akmod-tp_smapi

   These packages are required for advanced power management features provided by TLP on ThinkPad laptops.

Building and Executing Thermald on Fedora
-----------------------------------------

1. Install Dependencies
------------------------

To install the necessary dependencies, run the following commands:

.. code-block:: bash

    dnf install automake
    dnf install autoconf-archive
    dnf install gcc
    dnf install gcc-c++
    dnf install glib-devel
    dnf install dbus-glib-devel
    dnf install libxml2-devel
    dnf install gtk-doc
    dnf install upower-devel
    dnf install libevdev-devel

2. Build Thermald
-----------------

Clone the repository and build the project:

.. code-block:: bash

    git clone https://github.com/intel/thermal_daemon
    cd thermal_daemon
    ./autogen.sh prefix=/
    make
    sudo make install

The `prefix` value depends on the distribution version. It can be "/" or "/usr". 
Check the existing path of the thermald install, if present, to update and add the appropriate prefix.

3. Manage Thermald Service
--------------------------

To start the thermald service:

.. code-block:: bash

    sudo systemctl start thermald.service

To get the status of the thermald service:

.. code-block:: bash

    sudo systemctl status thermald.service

To stop the thermald service:

.. code-block:: bash

    sudo systemctl stop thermald.service


