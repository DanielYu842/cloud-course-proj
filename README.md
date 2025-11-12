# Setup Guide

### Step 1: Environment Setup

**For Local Setup:**
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Download Data

```bash
pip install requests
python scripts/download_data.py
```

This will download 6 files total:
- NYC: listings.csv + calendar.csv
- LA: listings.csv + calendar.csv  
- Paris: listings.csv + calendar.csv


### Step 3: Run the Analysis

Follow the notebooks in order:
1. `01_data_ingestion.ipynb` - Load and explore data
2. `02_data_cleaning.ipynb` - Clean and preprocess
3. `03_feature_engineering.ipynb` - Create features
4. `04_eda_analysis.ipynb` - Exploratory analysis
6. `05_model_training.ipynb` - Build ML models
7. `06_performance_eval.ipynb` - Spark benchmarks

---

## 📂 Project Structure Overview

```
cloud-project/
├── README.md              # Main project documentation
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
│
├── scripts/
│   └── download_data.py   # Automated data downloader
│
├── notebooks/             # Jupyter/Databricks notebooks
│
├── data/                  # Data directory (gitignored)
│   ├── raw/              # Original CSV files
│   │   ├── nyc/
│   │   ├── la/
│   │   └── paris/
│   └── processed/        # Cleaned datasets
│
├── outputs/              # Generated outputs
│   ├── figures/         # Plots and charts
│   ├── models/          # Saved ML models
│   └── results/         # Metrics and results

---
