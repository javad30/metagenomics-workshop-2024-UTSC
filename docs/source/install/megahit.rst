MEGAHIT (WSL)
===============

MEGAHIT is a fast and memory-efficient assembler for metagenomic sequencing data. There are several ways to install MEGAHIT, but the easiest way is using **conda**.  

On WSL systems, conda is often not installed by default, so you will need to install it first.

---

A) Install conda

1. Go to https://repo.anaconda.com/archive/ and download the appropriate installer for your system.  
   - For example, for WSL: ``Anaconda3-2024.06-1-Linux-x86_64.sh``

2. Open your terminal and download using `wget`:

   .. code-block:: bash

      wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh

3. Run the installation script:

   .. code-block:: bash

      bash Anaconda3-2024.06-1-Linux-x86_64.sh

4. Read the license agreement and follow the prompts to accept.  

5. Close WSL and open it again.  

6. Test that conda is installed:

   .. code-block:: bash

      conda

---

B) Install MEGAHIT using conda

.. code-block:: bash

   conda install -c bioconda megahit

- If prompted, select `y` to proceed.  
- Test the installation:

.. code-block:: bash

   megahit --help

- If this does not work, follow alternative installation methods:  
  https://github.com/voutcn/megahit

---

MEGAHIT (Mac)
===============

A) Install Miniconda

- Download the installer (pkg recommended) from:

  https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg

- Check installation:

.. code-block:: bash

   conda --version

- If prompted, select `y` to proceed.

B) Install MEGAHIT using conda

.. code-block:: bash

   conda install bioconda::megahit
