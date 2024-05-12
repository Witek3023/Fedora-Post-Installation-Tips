DNF Optimization
================
   
Configuration File Location
---------------------------

The configuration file is located at:

.. code-block:: plaintext

    /etc/dnf/dnf.conf

To edit it, you can use any text editor with administrator privileges:

.. code-block:: shell

    sudo nano /etc/dnf/dnf.conf

Default Selection "T" - Confirm Installation by Pressing Enter
----------------------------------------------------------------

.. code-block:: plaintext

    defaultyes=True

Package Download Optimization
------------------------------

.. code-block:: plaintext

    deltarpm=False
    metadata_timer_sync=3600
    max_parallel_downloads=10
    ip_resolve=4

Opting Out of "Weak Dependencies" Installation
-----------------------------------------------


.. code-block:: plaintext

    install_weak_deps=False
