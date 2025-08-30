Samtools
========

1. Convert SAM to BAM:

.. code-block:: bash

    samtools view -bS Mapped_and_unmapped_Solanaceae.sam > S28_mapped_and_unmapped.bam

2. Sort BAM file:

.. code-block:: bash

    samtools sort S28_mapped_and_unmapped.bam -o S28_sorted.bam

3. Create BAM index:

.. code-block:: bash

    samtools index S28_sorted.bam S28_sorted.bai
