Quickstart
==========

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


Trimming Sequence Data
----------------------

Adapter sequences should be removed as they interfere with downstream analyses. SRA files may include modifications incompatible with some pipelines. For trimming:

1. Identify your adapter sequence using **FastQC** or `grep`:

.. code-block:: bash

    grep AGATGTGTATAAGAGACAG SRR29754043_2.fastq

2. Download **Trimmomatic**: http://www.usadellab.org/cms/?page=trimmomatic (Version 0.39: binary)
3. Use the adapters file (e.g., `NexteraPE-PE.fa`) in your trimming command:

.. code-block:: bash

    java -jar trimmomatic-0.39.jar PE S28_R1.gz S28_R2.gz \
    output_forward_paired.fq.gz output_forward_unpaired.fq.gz \
    output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz \
    ILLUMINACLIP:NexteraPE-PE.fa:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:36


Removing Host Contaminants
---------------------------

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


Samtools
--------

1. Convert SAM to BAM:

.. code-block:: bash

    samtools view -bS Mapped_and_unmapped_Solanaceae.sam > S28_mapped_and_unmapped.bam

2. Sort BAM file:

.. code-block:: bash

    samtools sort S28_mapped_and_unmapped.bam -o S28_sorted.bam

3. Create BAM index:

.. code-block:: bash

    samtools index S28_sorted.bam S28_sorted.bai


Assembly
--------

Use **MEGAHIT** for assembly of metagenomic data:

.. code-block:: bash

    megahit -1 SAMPLE_R1.fastq -2 SAMPLE_R2.fastq -t 20 -o megahit_result


MetaBAT2 (Binning)
------------------

Upload the `final_contigs_file` from MEGAHIT to **Galaxy MetaBAT2**:  
https://usegalaxy.eu/?tool_id=toolshed.g2.bx.psu.edu/repos/iuc/metabat2/metabat2/2.15+galaxy1  

Or install MetaBAT2 via conda:

.. code-block:: bash

    conda install -c bioconda/label/cf201901::metabat2

Generate contig depth and run MetaBAT2:

.. code-block:: bash

    jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam
    metabat2 -i final.contigs.fa -a depth.txt -o bins_dir/bin


CheckM (Completeness and Contamination)
----------------------------------------

.. code-block:: bash

    checkm lineage_wf -x fa bins_dir/ METAG_checkm/ --threads 16 -f METAG-checkm.tsv --tab_table


Prodigal (Gene Prediction)
--------------------------

.. code-block:: bash

    prodigal -i my.metagenome.fna -o my.genes -a my.proteins.faa -p meta


Prokka (Genome Annotation)
---------------------------

.. code-block:: bash

    prokka --outdir mydir --prefix mygenome final.contigs13.fa


HTSeq (RNA-seq counting)
-------------------------

.. code-block:: bash

    htseq-count -r pos -t CDS -f bam S13.map.sorted.bam S13.gft > S13.count
