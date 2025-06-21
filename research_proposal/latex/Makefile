# Makefile for LaTeX compilation

# Variables
MAIN = research_proposal
OUTPUT = research_proposal
LATEX = pdflatex
BIBTEX = bibtex
OUTPUT_DIR = output

# Default target
all: $(OUTPUT_DIR)/$(OUTPUT).pdf

# Create output directory if it doesn't exist
$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

# Compile the document
$(OUTPUT_DIR)/$(OUTPUT).pdf: $(MAIN).tex references.bib | $(OUTPUT_DIR)
	$(LATEX) $(MAIN)
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN)
	$(LATEX) $(MAIN)
	cp $(MAIN).pdf $(OUTPUT_DIR)/$(OUTPUT).pdf
	rm $(MAIN).pdf

# Clean up auxiliary files
clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.lof *.lot *.dvi *.fls *.fdb_latexmk *.synctex.gz

# Clean up everything including the PDF
cleanall: clean
	rm -f $(OUTPUT_DIR)/$(OUTPUT).pdf

# Help target
help:
	@echo "Available targets:"
	@echo "  all      - Build the PDF document (default)"
	@echo "  clean    - Remove auxiliary files"
	@echo "  cleanall - Remove auxiliary files and the PDF"
	@echo "  help     - Display this help message"

.PHONY: all clean cleanall help