import sys
import urllib.request
import json
import csv
import os

gene = sys.argv[1]
organism = sys.argv[2]
output_file = sys.argv[3]

# Ensure output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene}+AND+organism_id:{organism}&format=json"

# Fetch data using urllib instead of requests
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

entry = data["results"][0]

domains = []

for f in entry.get("features", []):
    if f["type"] == "Region":
        desc = f.get("description", "").lower()

        if "domain" in desc or "binding" in desc:
            start = int(f["location"]["start"]["value"])
            end = int(f["location"]["end"]["value"])
            name = f.get("description", "Unknown")

            domains.append([name, start, end])

# Write CSV using built-in csv module
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Domain", "start", "end"])
    writer.writerows(domains)