# LaTeX Version of Garden AI Research Proposal

This directory contains the LaTeX source files for the Garden AI research proposal.

## Files

- `research_proposal.tex`: The main LaTeX document
- `references.bib`: BibTeX file containing all references
- `Makefile`: Makefile for easy compilation

## Compilation Instructions

### Using the Makefile (Recommended)

If you have `make` installed, you can use the following commands:

```bash
# Compile the document
make

# Clean up auxiliary files
make clean

# Clean up everything including the PDF
make cleanall

# Display help
make help
```

The compiled PDF will be placed in the `output` directory as `research_proposal.pdf`.

### Manual Compilation

If you don't have `make` installed, you can compile the document manually:

```bash
# First pass
pdflatex research_proposal

# Process bibliography
bibtex research_proposal

# Second pass
pdflatex research_proposal

# Third pass (to resolve all references)
pdflatex research_proposal
```

## Requirements

- A LaTeX distribution (e.g., TeX Live, MiKTeX)
- BibTeX
- The following LaTeX packages:
  - inputenc
  - geometry
  - graphicx
  - booktabs
  - array
  - enumitem
  - titlesec
  - fancyhdr
  - url
  - xcolor
  - float

Most modern LaTeX distributions include these packages by default.