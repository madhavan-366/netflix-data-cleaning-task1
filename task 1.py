import pandas as pd

# Load the raw dataset
file_path = "netflix_titles.csv"  
df = pd.read_csv(file_path)
# Track original stats
original_rows = df.shape[0]
original_duplicates = df.duplicated().sum()
null_counts_before = df.isnull().sum()

# 1. Remove duplicates
df = df.drop_duplicates()
rows_after_duplicates = df.shape[0]
# 2. Handle missing values
df['country'] = df['country'].fillna('Unknown')
df['director'] = df['director'].fillna('Not Available')
df['cast'] = df['cast'].fillna('Not Available')
df['rating'] = df['rating'].fillna('Unknown')
df['duration'] = df['duration'].fillna('Unknown')
# Track rows with missing date before dropping
null_date_rows = df['date_added'].isnull().sum()
df = df.dropna(subset=['date_added'])

# 3. Standardize text values
df['type'] = df['type'].str.strip().str.title()   # e.g., "Movie", "Tv Show"
df['rating'] = df['rating'].str.strip().str.upper()
# 4. Convert date formats
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# 5. Rename column headers
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 6. Ensure correct data types
df['release_year'] = df['release_year'].astype(int)
# Save cleaned dataset
output_file = "netflix_titles_cleaned.csv"
df.to_csv(output_file, index=False)
# ---- Summary Report ----
print("✅ Cleaning Complete!\n")
print("📊 Summary of Changes:")
print(f"- Original rows: {original_rows}")
print(f"- Duplicate rows removed: {original_duplicates}")
print(f"- Rows removed due to missing 'date_added': {null_date_rows}")
print(f"- Final rows: {df.shape[0]}")

print("\n- Missing values handled per column:")
for col in null_counts_before[null_counts_before > 0].index:
    print(f"   {col}: {null_counts_before[col]} → {df[col].isnull().sum()} after cleaning")

print("\n- Column names standardized to lowercase_with_underscores")
print("- 'date_added' converted to datetime format (YYYY-MM-DD)")
print("- Text fields like 'type' and 'rating' standardized")
print(f"\n💾 Cleaned dataset saved as: {output_file}")
