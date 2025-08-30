HTSeq Installation
===================

HTSeq is a Python library for analyzing high-throughput sequencing data.

---

A) Install via PIP

- To install the latest version from PyPI:

.. code-block:: bash

   pip install HTSeq

- To install a specific version (e.g., 2.0.0):

.. code-block:: bash

   pip install 'HTSeq==2.0.0'

- If this fails, make sure all dependencies are installed first:

.. code-block:: bash

   pip install matplotlib
   pip install Cython
   pip install pysam
   pip install HTSeq

---

B) Install via setup.py (distutils/setuptools)

1. Install dependencies with your preferred tool (pip, conda, etc.).  
2. Install HTSeq:

.. code-block:: bash

   python setup.py build install

---

C) Testing

- To test the full HTSeq installation locally:

.. code-block:: bash

   ./test.sh

- To test `htseq-count` alone:

.. code-block:: bash

   htseq-count -o output_file input_file

- A virtual environment is created in the `.venv` folder, and HTSeq is installed inside it, including all modules and scripts.
