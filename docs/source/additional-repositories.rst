Additional Repositories + Codecs
================================

RPM Fusion Repository Installation Guide
----------------------------------------

By default, Fedora, following its operating system policy, utilizes open-source software. To install closed-source software/drivers, you need to add the RPM Fusion repository.

Installation Steps
------------------

To install the RPM Fusion repository, execute the following code in the terminal:

.. code-block:: shell

    sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

AppStream Metadata
------------------

RPM Fusion repositories also provide Appstream metadata to enable users to install packages using Gnome Software/KDE Discover. Please note that these are a subset of all packages since the metadata are only generated for GUI packages.

For the current Fedora releases, the suggested method is to install appstream-data using DNF. Execute the following command to install the required packages:

.. code-block:: shell

    sudo dnf group upgrade core

Codecs Installation
--------------------

To ensure the complete FFMPEG is downloaded, execute the following command:

.. code-block:: shell

    sudo dnf swap ffmpeg-free ffmpeg --allowerasing
    sudo dnf install ffmpeg ffmpeg-libs libva libva-utils

Then install multimedia codecs:

.. code-block:: shell

    sudo dnf groupupdate multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
    sudo dnf groupupdate sound-and-video

Hardware Accelerated Codec Installation
----------------------------------------

For Intel (recent) hardware using the rpmfusion-nonfree section:

.. code-block:: shell

    sudo dnf install intel-media-driver

For older Intel hardware using the rpmfusion-free section:

.. code-block:: shell

    sudo dnf install libva-intel-driver

For AMD hardware (mesa) using the rpmfusion-free section:

.. code-block:: shell

    sudo dnf swap mesa-va-drivers mesa-va-drivers-freeworld
    sudo dnf swap mesa-vdpau-drivers mesa-vdpau-drivers-freeworld

If using i686 compat libraries (for steam or alikes):

.. code-block:: shell

    sudo dnf swap mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686
    sudo dnf swap mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686

OpenH264 Installation
---------------------

To enable OpenH264, execute the following commands:

.. code-block:: shell

    sudo dnf config-manager --enable fedora-cisco-openh264
    sudo dnf install gstreamer1-plugin-openh264 mozilla-openh264

Troubleshooting
---------------

If you encounter issues with displaying images, photos, or sound in applications or games, it's likely due to missing libraries (codecs). To fix this issue, you can use the following commands:

Install GStreamer plugins:

.. code-block:: shell

    sudo dnf install gstreamer1-plugins-{bad-\*,good-\*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel

Install Lame:

.. code-block:: shell

    sudo dnf install lame\* --exclude=lame-devel

Upgrade Multimedia group:

.. code-block:: shell

    sudo dnf group upgrade --with-optional Multimedia

Flathub - the Largest Flatpak Software Repository
--------------------------------------------------
Apart from DNF, there's another future-oriented alternative for traditional package managers.
There are two branches of the Flathub repository - stable and beta. Both repositories complement each other,

To add Flathub Stable, execute the following command:

.. code-block:: shell

    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

To add Flathub Beta, execute the following command:

.. code-block:: shell

    flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
