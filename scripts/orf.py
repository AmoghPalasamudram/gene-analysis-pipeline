import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f:
    seq = f.read().strip()

start = "ATG"
stops = ["TAA", "TAG", "TGA"]

orfs = []

for i in range(len(seq)):
    if seq[i:i+3] == start:
        for j in range(i, len(seq), 3):
            if seq[j:j+3] in stops:
                orfs.append((i, j+3))
                break

df = pd.DataFrame(orfs, columns=["Start", "End"])
df.to_csv(output_file, index=False)