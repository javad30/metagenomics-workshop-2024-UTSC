Trimming Sequence Data
======================

Adapter sequences should be removed as they interfere with downstream analyses. SRA files may include modifications incompatible with some pipelines. For trimming:

1. Identify your adapter sequence using **FastQC** or ``grep``:

.. code-block:: bash

    grep AGATGTGTATAAGAGACAG SRR29754043_2.fastq

2. Download **Trimmomatic**: http://www.usadellab.org/cms/?page=trimmomatic (Version 0.39: binary)

3. Use the adapters file (e.g., ``NexteraPE-PE.fa``) in your trimming command:

.. code-block:: bash

    java -jar trimmomatic-0.39.jar PE S28_R1.gz S28_R2.gz \
      output_forward_paired.fq.gz output_forward_unpaired.fq.gz \
      output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz \
      ILLUMINACLIP:NexteraPE-PE.fa:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:36
