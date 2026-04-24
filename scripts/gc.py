import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f:
    seq = f.read().strip()

gc = (seq.count("G") + seq.count("C")) / len(seq) * 100

with open(output_file, "w") as f:
    f.write(str(gc))