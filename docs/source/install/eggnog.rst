eggNOG-mapper Installation
==========================

eggNOG-mapper is a tool for fast functional annotation of novel sequences using precomputed orthologous groups and functional information.

Requirements
------------

### Software Requirements

- Python 3.7 or greater
- BioPython >=1.76 (1.78 should also work for emapper v2.1.7)
- psutil >=5.7.0
- xlsxwriter >=1.4.3 (only if using the --excel option)
- wget (Linux command; required for downloading databases with `download_eggnog_data.py` or creating new Diamond/MMseqs2 databases)
- sqlite >=3.8.2

### Storage Requirements

- ~40 GB for the eggNOG annotation databases (`eggnog.db` and `eggnog.taxa.db`)
- ~9 GB for Diamond database (required if using `-m diamond`)
- ~11 GB for MMseqs2 database (~86 GB if full MMseqs2 index is created; required if using `-m mmseqs`)
- ~3 GB for PFAM database (required if using `--pfam_realign` options)

Database sizes depend on the selected taxonomic range. See:
- HMMER databases: http://eggnog5.embl.de/#/app/downloads  
- Diamond/MMseqs2 databases: size depends on number of proteins in the taxonomic range

### Memory Requirements

- Using `--dbmem` loads the entire `eggnog.db` into memory (~44 GB required)
- Using `--num_servers` when running HMMER in server mode may increase memory usage proportionally

Installation
------------

### PyPI Version

.. code-block:: bash

   pip install eggnog-mapper

To install a specific version:

.. code-block:: bash

   pip install 'eggnog-mapper==<version>'

### Conda (Bioconda Channel)

.. code-block:: bash

   conda install -c bioconda -c conda-forge eggnog-mapper

### GitHub Release

1. Download the latest version:  
   https://github.com/eggnogdb/eggnog-mapper/releases/latest
2. Decompress the `.tar.gz` or `.zip` file
3. Enter the decompressed directory and install dependencies:

.. code-block:: bash

   # Using setuptools
   python setup.py install

   # Using pip
   pip install -r requirements.txt

   # Using conda
   conda install --file requirements.txt

### Cloning from GitHub

.. code-block:: bash

   git clone https://github.com/eggnogdb/eggnog-mapper.git
   cd eggnog-mapper
   # Then install dependencies as above

Setup
-----

Add eggNOG-mapper scripts and binaries to your PATH for convenience:

.. code-block:: bash

   export PATH=/home/user/eggnog-mapper:/home/user/eggnog-mapper/eggnogmapper/bin:"$PATH"

Optionally, define a directory for the eggNOG-mapper databases:

.. code-block:: bash

   export EGGNOG_DATA_DIR=/home/user/eggnog-mapper-data

Download the databases:

.. code-block:: bash

   download_eggnog_data.py

- By default, files are downloaded to `data/` within the eggNOG-mapper directory if no `EGGNOG_DATA_DIR` or `--data_dir` is specified.
- The Diamond database is optional; you can also use HMMER or MMseqs2.
- For taxonomic-specific Diamond/MMseqs2 databases, use:

.. code-block:: bash

   create_dbs.py -m diamond --dbname bacteria --taxa Bacteria

Optional Tools
--------------

eggNOG-mapper can use bundled binaries for the following tools:

- **Prodigal**: required for `--itype genome` or `--itype metagenome` with `--genepred prodigal`
- **Diamond**: required for `-m diamond` searches
- **MMseqs2**: required for `-m mmseqs` searches
- **HMMER**: required for `-m hmmer` and PFAM realignment options

If the tools are already installed on your system, eggNOG-mapper will use the versions found in your PATH. Otherwise, it uses the bundled binaries.
