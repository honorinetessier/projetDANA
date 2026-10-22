import pandas as pd

# Project folders
input_file = "../CSV/france_all_features.csv"
output_file = "../CSV/clean_france_all_features.csv"

# 1. Read CSV
df = pd.read_csv(
    input_file,
    dtype=str,
    keep_default_na=False
)

# Clean column names
df.columns = df.columns.str.strip().str.strip("'").str.strip('"')

print("Initial number of rows:", len(df))
print("Initial columns:")
print(df.columns.tolist())


# 2. Remove unnecessary columns
columns_to_remove = [
    "alternatenames",
    "cc2",
    "admin2_code",
    "admin3_code",
    "admin4_code",
    "dem_gtopo30",
    "modification_date"
]

df = df.drop(columns=columns_to_remove, errors="ignore")


# 3. Remove completely empty rows
df = df.dropna(how="all")


# 4. Clean spaces
for column in df.columns:
    df[column] = df[column].str.strip()


# 5. Remove rows without a GeoNames ID
df = df[df["geonameid"] != ""]


# 6. Remove duplicated GeoNames IDs
df = df.drop_duplicates(subset=["geonameid"])


# 7. Convert numeric columns
numeric_columns = [
    "latitude",
    "longitude",
    "population",
    "elevation"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# 8. Validate coordinates
df = df[
    df["latitude"].between(-90, 90, inclusive="both")
    & df["longitude"].between(-180, 180, inclusive="both")
]


# 9. Validate population
df = df[
    (df["population"].isna()) |
    (df["population"] >= 0)
]


# 10. Save cleaned dataset
df.to_csv(
    output_file,
    index=False,
    encoding="utf-8"
)


print("\nCleaning completed.")
print("Final number of rows:", len(df))
print("Final columns:")
print(df.columns.tolist())
print("\nOutput:", output_file)