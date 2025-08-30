Obtaining Sequence Data
=======================

You can either bring your sequence of interest or download sequences from online resources. One of the most useful online resources is the **NCBI SRA**. To do so:

1. Go to the NCBI SRA website: https://www.ncbi.nlm.nih.gov/sra and search for species/project.
2. After finding the BioProject/sequence you want, copy the **SRA ID** under the **RUN** tab.
3. Install the SRA toolkit on your system (Mac, Ubuntu, etc.):

.. code-block:: bash

    sudo apt install sra-toolkit

4. Download the sequence using the SRA ID (example: SRR29754043):

.. code-block:: bash

    prefetch SRR29754043
    fastq-dump --split-files SRR29754043 -O /your/output/folder
    cd /your/output/folder

5. Check the quality of the fastq files using **FastQC**:

.. code-block:: bash

    fastqc *fastq -O SRA_fastq
