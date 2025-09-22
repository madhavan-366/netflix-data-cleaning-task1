# netflix-data-cleaning-task1

## Objective
Clean and prepare a raw Netflix dataset by handling missing values, duplicates, inconsistent formats, and data types.

## Tools
- Python (Pandas)

## Steps Performed
1. Removed duplicate rows.
2. Handled missing values (e.g., filled with 'Unknown' or 'Not Available').
3. Standardized text values (e.g., `type`, `rating`).
4. Converted `date_added` to datetime format.
5. Renamed column headers to lowercase with underscores.
6. Ensured correct data types (e.g., `release_year` as int).
7. Saved the cleaned dataset.

## Deliverables
- `task1_cleaning.py` → Python script for cleaning
- `netflix_titles.csv` → Raw dataset
- `netflix_titles_cleaned.csv` → Cleaned dataset
- `screenshots/` → Folder with screenshots

