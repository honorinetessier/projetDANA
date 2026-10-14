import csv
import math

# Project folders
input_file = "../CSV/allCountries.csv"
output_file = "../CSV/nantes_100km.csv"


# Nantes coordinates will be found from GeoNames itself
NANTES_NAME = "Nantes"
RADIUS_KM = 100


def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points in kilometers."""
    earth_radius = 6371.0

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.asin(math.sqrt(a))

    return earth_radius * c


# --------------------------------------------------
# Step 1: Find Nantes
# --------------------------------------------------

nantes_lat = None
nantes_lon = None

print("Searching for Nantes...")

with open(input_file, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if (
            row["name"].strip().lower() == NANTES_NAME.lower()
            and row["country_code"] == "FR"
        ):
            nantes_lat = float(row["latitude"])
            nantes_lon = float(row["longitude"])

            print(
                f"Nantes found: latitude={nantes_lat}, "
                f"longitude={nantes_lon}"
            )
            break


if nantes_lat is None:
    raise ValueError("Nantes was not found in allCountries.csv")


# --------------------------------------------------
# Step 2: Filter features within 30 km
# --------------------------------------------------

print(f"Filtering features within {RADIUS_KM} km of Nantes...")

with open(input_file, "r", encoding="utf-8", newline="") as input_csv:

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

        count = 0

        for row in reader:

            try:
                latitude = float(row["latitude"])
                longitude = float(row["longitude"])
            except (ValueError, TypeError):
                continue

            distance = haversine_distance(
                nantes_lat,
                nantes_lon,
                latitude,
                longitude
            )

            if distance <= RADIUS_KM:
                writer.writerow(row)
                count += 1


print()
print("Filtering completed.")
print(f"Number of features: {count}")
print(f"Output file: {output_file}")