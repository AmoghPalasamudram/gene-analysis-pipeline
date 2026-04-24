import sys
import csv
import os

gc_file = sys.argv[1]
orfs_file = sys.argv[2]
domains_file = sys.argv[3]
output_file = sys.argv[4]

os.makedirs(os.path.dirname(output_file), exist_ok=True)

# --- Read GC content ---
with open(gc_file) as f:
    gc_content = f.read().strip()

# --- Count ORFs ---
orf_count = 0
with open(orfs_file) as f:
    reader = csv.reader(f)
    next(reader, None)  # skip header if exists
    for _ in reader:
        orf_count += 1

# --- Count domains ---
domain_count = 0
with open(domains_file) as f:
    reader = csv.reader(f)
    next(reader, None)  # skip header
    for _ in reader:
        domain_count += 1

# --- Write summary ---
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Metric", "Value"])
    writer.writerow(["GC_Content", gc_content])
    writer.writerow(["ORF_Count", orf_count])
    writer.writerow(["Domain_Count", domain_count])