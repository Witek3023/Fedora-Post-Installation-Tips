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

5. Configure Zsh by replacing the `.zshrc` file with your custom configuration.

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

Additional Software Installation and Configuration
---------------------------------------------------

1. **Install essential(fully personal) tools:**

   .. code-block:: shell

      sudo dnf install net-tools pip htop neofetch kitty git unzip btop zathura feh ranger vim emacs figlet lolcat perl-Archive-Extract-lzma-IO-Uncompress-UnLzma tar xz p7zip zip gzip cpio unace inxi stow sl cmus

2. **Set hardware clock to local time:**

   .. code-block:: shell

        sudo timedatectl set-local-rtc '0'

   Ensures the hardware clock is set to UTC for better time synchronization.

3. **Disable terminal bell**
    .. code-block:: shell

        echo "blacklist pcspkr" | sudo tee /etc/modprobe.d/blacklist-pcspkr.conf > /dev/null

5. **Installing Visual Studio Code on Fedora**

To install Visual Studio Code on RHEL, Fedora, or CentOS, follow these steps:

1. **Import the Microsoft GPG Key**

   Import the Microsoft GPG key by running the following command:

   .. code-block:: bash

      sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc

2. **Add the VS Code Repository**

   Create a repository file for VS Code with the following command:

   .. code-block:: bash

      echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo > /dev/null

3. **Update the Package Cache and Install**

   Update the package cache and install Visual Studio Code:

   .. code-block:: bash

      dnf check-update
      sudo dnf install code  # or code-insiders


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
Install tuned-ppd or TLP
**For tuned-ppd**
Replace power-profiles-daemon with tuned-ppd:

.. code-block:: shell
    sudo dnf swap power-profiles-daemon tuned-ppd

**For TLP**
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

1. **Install Dependencies**


To install the necessary dependencies, run the following commands:

.. code-block:: bash

    dnf install automake libevdev-devel upower-devel gtk-doc libxml2-devel dbus-glib-devel glib-devel gcc-c++ gcc autoconf-archive

2. **Build Thermald**

Clone the repository and build the project:

.. code-block:: bash

    git clone https://github.com/intel/thermal_daemon
    cd thermal_daemon
    ./autogen.sh prefix=/
    make
    sudo make install

The `prefix` value depends on the distribution version. It can be "/" or "/usr". 
Check the existing path of the thermald install, if present, to update and add the appropriate prefix.

3. **Manage Thermald Service**


To enable the thermald service:

.. code-block:: bash

    sudo systemctl enable thermald.service
    sudo systemctl start thermald.service

To get the status of the thermald service:

.. code-block:: bash

    sudo systemctl status thermald.service

To stop the thermald service:

.. code-block:: bash

    sudo systemctl stop thermald.service

-----------------------
How to Make KDE Faster
-----------------------

This document provides steps to optimize KDE's performance by configuring Baloo, desktop effects, background services, Plasma search, general behavior animation speed, and user feedback settings.

Baloo Configuration
--------------------

Baloo is KDE's file indexing and search service. Disabling or optimizing it can improve performance.

1. **Disable Baloo:**

   To disable Baloo, run the following command in the terminal:

   .. code-block:: bash

      balooctl6 disable

2. **Optimize Baloo:**

   If you prefer to keep Baloo enabled but want to optimize its performance, you can exclude certain file types and directories from being indexed. Edit the Baloo configuration file:

   .. code-block:: bash

      kate ~/.config/baloofilerc

disabling Akonadi
-----------------
    Run to stop currently running server

    .. code-block:: bash
        akonadictl stop
    
    Edit `/$HOME/.config/akonadi/akonadiserverrc` and change `true` to `false` in the line that has `StartServer=true`

Desktop Effects
-----------------

Disabling or reducing desktop effects can significantly speed up KDE.

1. **Access Desktop Effects:**

   Open System Settings and navigate to ``Apps % Windows`` > ``Window Manager`` > ``Desktop Effects``.

2. **Disable Unnecessary Effects:**

   Uncheck effects that you don't need, such as ``Blur``, ``Fade``, and ``Sliding Popups``.

Background Services
---------------------

Disabling unnecessary background services can free up system resources.

1. **Access Background Services:**

   Open System Settings and search for ``Background Services``.

2. **Disable Unnecessary Services:**

   Review the list of services and disable those that are not needed. For example, ``Vaults``, ``Remote URL change notifier``, ``SMB Watcher`` and ``Write Daemon`` services may be unnecessary for some users.

Plasma Search
---------------

Configuring Plasma Search to index fewer items can improve performance.

1. **Access Plasma Search:**

   Open System Settings and navigate to ``Workspace`` > ``Search`` > ``Plasma Search``.

2. **Configure Search:**

   Uncheck the categories and types of files you don't need indexed. This can reduce the overhead of the search indexing process.

General Behavior Animation Speed
----------------------------------

Reducing or disabling animations can make the desktop feel more responsive.

1. **Access General Behavior Settings:**

   Open System Settings and navigate to ``Workspace`` > ``General Behavior``.

2. **Set Animation Speed:**

   Change the ``Animation speed`` to ``Instant`` to disable animations or select a faster option.

User Feedback
---------------

Disabling user feedback can reduce background processing.

1. **Access User Feedback Settings:**

   Open System Settings and navigate to ``Security & Privacy`` > ``User Feedback``.

2. **Disable User Feedback:**

   Set the ``User Feedback`` level to ``None``.

By following these steps, you can optimize KDE's performance and enjoy a faster, more responsive desktop environment.
