Installing CheckM (WSL)
========================

CheckM is a tool for assessing the quality of metagenome-assembled genomes (MAGs).  

---

A) Create a conda environment and install dependencies

.. code-block:: bash

   conda create -n checkm python=3.9
   conda activate checkm
   conda install -c bioconda numpy matplotlib pysam
   conda install -c bioconda hmmer prodigal pplacer
   pip3 install checkm-genome

---

B) Download reference data

- Download the reference dataset from Zenodo:

  https://zenodo.org/records/7401545#.Y44ymHbMJD8

- Set the environment variable to point to the reference data:

.. code-block:: bash

   export CHECKM_DATA_PATH=/path/to/my_checkm_data

---

Installing CheckM (Mac)
========================

A) Install dependencies using Homebrew

.. code-block:: bash

   brew install hmmer
   brew install prodigal
   brew install pplacer

B) Install Python packages

.. code-block:: bash

   pip3 install numpy
   pip3 install matplotlib
   pip3 install pysam
   pip3 install checkm-genome

C) Download reference data

- Download the reference dataset from Zenodo:

  https://zenodo.org/records/7401545#.Y44ymHbMJD8

- Set the environment variable to point to the reference data:

.. code-block:: bash

   export CHECKM_DATA_PATH=/path/to/my_checkm_data
