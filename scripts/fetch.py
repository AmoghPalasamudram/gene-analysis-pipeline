import sys
import requests

gene = sys.argv[1]
organism = sys.argv[2]
output_file = sys.argv[3]

url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene}+AND+organism_id:{organism}&format=json"

data = requests.get(url).json()

sequence = data["results"][0]["sequence"]["value"]

with open(output_file, "w") as f:
    f.write(sequence)