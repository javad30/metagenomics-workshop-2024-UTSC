# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = "Metagenomics Workshop 2024 UTSC"
author = "Javad Sadeghi"
release = "0.1"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",    # Automatically document docstrings
    "sphinx.ext.napoleon",   # Support Google/NumPy style docstrings
    "sphinx.ext.viewcode",   # Add links to source code
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,   # keep sections expanded
    "navigation_depth": 2,          # show subpages like fastqc, bowtie2, etc.
    "titles_only": True,            # cleaner sidebar (no duplicate headings)
}

# -- Workaround for heavy imports on RTD -------------------------------------
# These packages are mocked so autodoc won't try to import them on RTD
autodoc_mock_imports = [
    "numpy",
    "pandas",
    "scikit-bio",
    "biom-format",
]
