
Installing FastQC on Linux
==========================

Installing **FastQC** on a Linux system is simple and only takes a few steps.

Update your system
------------------
First, update your package list to make sure you have the latest software references:

.. code-block:: bash

   sudo apt update

Install FastQC
--------------
With your package list updated, install FastQC:

.. code-block:: bash

   sudo apt install fastqc

This command will download and install FastQC on your system.

Verify the installation
-----------------------
To confirm that FastQC has been installed correctly, run:

.. code-block:: bash

   fastqc --help

If successful, this will display the help information and version number.

----

After completing these steps, FastQC will be installed and ready for use on your Linux system, setting the stage for high-quality sequence data analysis.


----

Installing FastQC on macOS
==========================

On macOS, the easiest way to install **FastQC** is through Homebrew.

Install Homebrew
----------------
If you don’t already have Homebrew installed, you can either:

- Visit the Homebrew website: https://brew.sh/ and follow the instructions, or  
- Run the following command directly in your terminal:

.. code-block:: bash

   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install FastQC
--------------
Once Homebrew is installed, use it to install FastQC:

.. code-block:: bash

   brew install fastqc

This step may take up to 5 minutes.

Verify the installation
-----------------------
To confirm that FastQC was installed correctly, run:

.. code-block:: bash

   fastqc --help

If successful, this will display the FastQC help information and version number.