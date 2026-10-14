import csv

input_file = "../Raw/allCountries.txt"
output_file = "../CSV/allCountries.csv"

#input_file = "../Raw/cities1000.txt"
#output_file = "../CSV/cities1000.csv"

columns = [
    "geonameid ",
    "name",
    "asciiname",
    "alternatenames",
    "latitude",
    "longitude",
    "feature_class",
    "feature_code",
    "country_code",
    "cc2",
    "admin1_code",
    "admin2_code",
    "admin3_code",
    "admin4_code",
    "population",
    "elevation",
    "dem_gtopo30",
    "timezone",
    "modification_date"
]

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8", newline="") as outfile:

    reader = csv.reader(infile, delimiter="\t")
    writer = csv.writer(outfile)

    writer.writerow(columns)

    for row in reader:
        writer.writerow(row)

print("Conversion completed!")
print("Output:", output_file)

with open(output_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("Number of columns:", len(header))
    print("Columns:", header)