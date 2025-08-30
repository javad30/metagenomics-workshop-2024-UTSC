MetaBAT2 (Binning)
==================

Upload the ``final_contigs_file`` from MEGAHIT to **Galaxy MetaBAT2**:
https://usegalaxy.eu/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/metabat2/metabat2/2.15+galaxy1

Or install MetaBAT2 via conda:

.. code-block:: bash

    conda install -c bioconda/label/cf201901::metabat2

Generate contig depth and run MetaBAT2:

.. code-block:: bash

    jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam
    metabat2 -i final.contigs.fa -a depth.txt -o bins_dir/bin
