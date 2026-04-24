import csv
import os

input_file = snakemake.input[0]
output_file = snakemake.output[0]

# Ensure output folder exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Read all rows first
with open(input_file) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Handle empty case
if not rows:
    with open(output_file, "w") as f:
        f.write("<h2>No domains found</h2>")
    exit()

# Get max protein length
max_end = max(int(row['end']) for row in rows)

# Visualization settings
container_width = 900
colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"]

# Start HTML
html = f"""
<h2 style="font-family:Arial;">Protein Domain Architecture: {snakemake.config['gene']}</h2>

<div style='
    width:{container_width}px;
    border:2px solid black;
    position:relative;
    height:60px;
    background-color:#f5f5f5;
'>
"""

# Plot domains
for i, row in enumerate(rows):
    start = int(row['start'])
    end = int(row['end'])
    width = end - start

    # Normalize positions
    left = int((start / max_end) * container_width)
    scaled_width = max(5, int((width / max_end) * container_width))  # minimum width for visibility

    color = colors[i % len(colors)]

    html += f"""
    <div style='
        position:absolute;
        left:{left}px;
        width:{scaled_width}px;
        height:40px;
        background-color:{color};
        border:1px solid black;
        border-radius:5px;
        color:white;
        font-size:10px;
        text-align:center;
        white-space:nowrap;
        overflow:hidden;
    '>
        {row['Domain'][:12]}
    </div>
    """

# Close container
html += "</div>"

# Footer
html += """
<p style="font-family:Arial; font-size:12px;">
Each block represents a detected protein domain scaled to protein length.
</p>
"""

# Save HTML
with open(output_file, "w") as f:
    f.write(html)