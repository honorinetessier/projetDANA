import csv
from pathlib import Path


# Project folders
input_file = "../CSV/allCountries.csv"
output_file = "../CSV/france_all_features.csv"


print("Starting France filtering...")
print(f"Input: {input_file}")
print(f"Output: {output_file}")

count = 0

with open(
    input_file,
    "r",
    encoding="utf-8",
    newline=""
) as input_csv:

    reader = csv.DictReader(input_csv)

    fieldnames = reader.fieldnames

    with open(
        output_file,
        "w",
        encoding="utf-8",
        newline=""
    ) as output_csv:

        writer = csv.DictWriter(
            output_csv,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for row in reader:

            # Keep every GeoNames feature located in France
            if row["country_code"] != "FR":
                continue

            writer.writerow(row)
            count += 1

            if count % 10000 == 0:
                print(f"{count} French features found...")


print()
print("Filtering completed.")
print(f"Total French features: {count}")
print(f"Output file: {output_file}")