Prodigal Installation
=====================

Prodigal is a fast and accurate gene prediction tool designed for prokaryotic genomes. It identifies protein-coding genes in microbial DNA sequences.

---

A) Install using Conda (Recommended)

.. code-block:: bash

   conda install -c bioconda prodigal

- This installs Prodigal from the Bioconda channel, handling all dependencies automatically.  
- Test the installation:

.. code-block:: bash

   prodigal -v

---

B) Install using Homebrew (macOS)

.. code-block:: bash

   brew install prodigal

- Test the installation:

.. code-block:: bash

   prodigal -v

---

C) Compile from Source (Linux / Unix)

1. Download the latest release from the Prodigal GitHub releases page:  
   https://github.com/hyattpd/Prodigal/releases

2. Extract the tar.gz file:

.. code-block:: bash

   tar -xzf prodigal-<version>.tar.gz
   cd prodigal-<version>

3. Compile the program:

.. code-block:: bash

   make

4. Optionally, install system-wide:

.. code-block:: bash

   sudo make install

- Ensure the executable is in your PATH to run it from any directory.
