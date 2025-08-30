Removing Host Contaminants
==========================

Sometimes host DNA is present. For example, in tomato microbiome studies, remove tomato DNA using **Bowtie2**:

1. Download host genome (e.g., tomato) from NCBI.
2. Index the host genome:

.. code-block:: bash

    bowtie2-build Solanaceae.fna Solanaceae --threads 20

3. Remove host reads:

.. code-block:: bash

    bowtie2 -x 0_Host_genome/Solanaceae/Solanaceae \
      -1 S28_R1.gz -2 S28_R2.gz --un-conc-gz S28_removed_Solanaceae \
      -S Mapped_and_unmapped_Solanaceae.sam -p 20 --very-sensitive-local

4. Rename files for downstream processing:

.. code-block:: bash

    mv S28_removed_Solanaceae.1 S28_host_removed_R1.fastq.gz
    mv S28_removed_Solanaceae.2 S28_host_removed_R2.fastq.gz
