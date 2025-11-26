# Project Report Compilation Guide

This directory contains the COMP4651 project report in two formats:
- `report.tex` - LaTeX source file (professional formatting)
- `report.md` - Markdown version (for easy viewing and alternative PDF conversion)

## Option 1: Compile LaTeX to PDF (Recommended)

### macOS
```bash
# Install MacTeX (if not installed)
brew install --cask mactex

# Compile (run twice for proper references)
cd report
pdflatex report.tex
pdflatex report.tex
```

### Linux (Ubuntu/Debian)
```bash
# Install TeX Live
sudo apt-get install texlive-full

# Compile
cd report
pdflatex report.tex
pdflatex report.tex
```

### Windows
1. Install MiKTeX from https://miktex.org/
2. Open MiKTeX Console and compile `report.tex`

### Online (No Installation Required)
1. Go to [Overleaf](https://www.overleaf.com/)
2. Create a new project
3. Upload `report.tex`
4. Click "Recompile" to generate PDF
5. Download the PDF

## Option 2: Convert Markdown to PDF

### Using Pandoc
```bash
# Install pandoc
brew install pandoc  # macOS
# OR
sudo apt-get install pandoc  # Linux

# Convert to PDF
pandoc report.md -o report.pdf --pdf-engine=pdflatex
```

### Using VS Code
1. Install "Markdown PDF" extension
2. Open `report.md`
3. Press `Cmd+Shift+P` → "Markdown PDF: Export (pdf)"

### Using Online Tools
1. Go to https://md2pdf.netlify.app/ or https://dillinger.io/
2. Paste the markdown content
3. Export as PDF

## Report Contents

The report covers:
1. **Abstract** - Project summary
2. **Introduction** - Motivation, problem statement, objectives
3. **System Design** - Architecture, technology stack, Spark configuration
4. **Implementation** - Data pipeline, cleaning, feature engineering, ML pipeline
5. **Experiments & Results** - EDA, ML model comparison, Spark performance
6. **Conclusions** - Key findings, limitations, future work
7. **References** - Academic and technical sources

## Word Count
Approximately 4,200 words (excluding references), within the 5,000 word limit.

## Figures
The report references figures from `../outputs/figures/`. To include them in the LaTeX PDF, ensure the figures directory is accessible during compilation.

