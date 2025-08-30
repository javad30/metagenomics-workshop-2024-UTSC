Installing Bowtie2
==================

Bowtie2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences.  
It works particularly well for reads of about 50 up to hundreds of bases aligned to relatively long genomes (e.g., mammalian).  
In my opinion, Bowtie2 is one of the most important software tools in genomics (cited ~50K times).  
Read more about Bowtie2 here: https://bowtie-bio.sourceforge.net/bowtie2/manual.shtml

Bowtie2 on Ubuntu/Linux
-----------------------

There are multiple ways to install Bowtie2. Two common methods are described below:

**a) Install using conda**

.. code-block:: bash

   conda install -c bioconda bowtie2

**b) Install using the package manager (recommended)**

.. code-block:: bash

   sudo apt update
   sudo apt install bowtie2

**c) Verify the installation**

.. code-block:: bash

   bowtie2 --help

If successful, this will display Bowtie2 help information and version number.

----

Bowtie2 on macOS
----------------

**A. Check if Homebrew is installed**

Run:

.. code-block:: bash

   brew --help

If you get `command not found`, you need to install Homebrew first.  
Refer to the *Installing FastQC on macOS* section for instructions on installing Homebrew.  

**B. Install Bowtie2 using Homebrew**

.. code-block:: bash

   brew install bowtie2

**C. Verify the installation**

.. code-block:: bash

   bowtie2

If successful, this will display Bowtie2 usage information and version number.
