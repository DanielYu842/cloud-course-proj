#!/usr/bin/env python3

import requests
import gzip
import shutil
from pathlib import Path
import sys

DATASETS = {
    'nyc': {
        'listings': 'https://data.insideairbnb.com/united-states/ny/new-york-city/2025-10-01/data/listings.csv.gz',
        'calendar': 'https://data.insideairbnb.com/united-states/ny/new-york-city/2025-10-01/data/calendar.csv.gz'
    },
    'la': {
        'listings': 'https://data.insideairbnb.com/united-states/ca/los-angeles/2025-09-01/data/listings.csv.gz',
        'calendar': 'https://data.insideairbnb.com/united-states/ca/los-angeles/2025-09-01/data/calendar.csv.gz'
    },
    'paris': {
        'listings': 'https://data.insideairbnb.com/france/ile-de-france/paris/2024-12-06/data/listings.csv.gz',
        'calendar': 'https://data.insideairbnb.com/france/ile-de-france/paris/2024-12-06/data/calendar.csv.gz'
    }
}


def download_file(url, output_path):
    print(f"Downloading: {url}")
    print(f"Saving to: {output_path}")
    
    try:
        response = requests.get(url, stream=True, timeout=300)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        
        downloaded = 0
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
        
        print()
        print(f"Downloaded successfully")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")
        return False


def extract_gz(gz_path, output_path):    
    try:
        with gzip.open(gz_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        gz_path.unlink()
        
        size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"Extracted: {output_path.name} ({size_mb:.1f} MB)")
        return True
        
    except Exception as e:
        print(f"Extraction failed: {e}")
        return False


def main():
    print("Downloading listings and calendar data for NYC, LA, and Paris")
    print()
    
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent / 'data' / 'raw'
    total_files = len(DATASETS) * 2  # 2 files per city
    successful = 0
    skipped = 0
    failed = 0
    
    for city, urls in DATASETS.items():
        city_dir = base_dir / city
        city_dir.mkdir(parents=True, exist_ok=True)
        
        print(city.upper())
        
        for file_type, url in urls.items():
            gz_path = city_dir / f"{file_type}.csv.gz"
            csv_path = city_dir / f"{file_type}.csv"
            
            if csv_path.exists():
                size_mb = csv_path.stat().st_size / (1024 * 1024)
                skipped += 1
                continue
            
            if download_file(url, gz_path):
                if extract_gz(gz_path, csv_path):
                    successful += 1
                else:
                    failed += 1
            else:
                failed += 1
            
            print()
    
    print(f"downloaded: {successful}")
    print(f"skipped (already exist): {skipped}")
    print(f"failed: {failed}")
    
    if failed > 0:
        print("some downloads failed")
        sys.exit(1)
    elif successful + skipped == total_files:
        print("all files ready")
        sys.exit(0)
    else:
        print("some downloads failed")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        sys.exit(1)

