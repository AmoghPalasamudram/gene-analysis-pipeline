configfile: "config.yaml"

# Get inputs
GENE = config["gene"]
ORG = config["organism_id"]

# -------------------------
# Final target
# -------------------------
rule all:
    input:
        f"results/{GENE}/gc.txt",
        f"results/{GENE}/orfs.csv",
        f"results/{GENE}/domains.csv",
        f"results/{GENE}/summary.csv",
        f"results/{GENE}/domain_plot.html"

# -------------------------
# Fetch sequence
# -------------------------
rule fetch_sequence:
    output:
        f"data/{GENE}_sequence.txt"
    shell:
        "python scripts/fetch.py {GENE} {ORG} {output}"


# -------------------------
# GC content
# -------------------------
rule compute_gc:
    input:
        f"data/{GENE}_sequence.txt"
    output:
        f"results/{GENE}/gc.txt"
    shell:
        "python scripts/gc.py {input} {output}"


# -------------------------
# ORF detection
# -------------------------
rule find_orfs:
    input:
        f"data/{GENE}_sequence.txt"
    output:
        f"results/{GENE}/orfs.csv"
    shell:
        "python scripts/orf.py {input} {output}"


# -------------------------
# Fetch domains
# -------------------------
rule fetch_domains:
    output:
        f"results/{GENE}/domains.csv"
    shell:
        "python scripts/domain.py {GENE} {ORG} {output}"


# -------------------------
# Summary
# -------------------------
rule summary:
    input:
        gc=f"results/{GENE}/gc.txt",
        orfs=f"results/{GENE}/orfs.csv",
        domains=f"results/{GENE}/domains.csv"
    output:
        f"results/{GENE}/summary.csv"
    shell:
        "python scripts/summary.py {input.gc} {input.orfs} {input.domains} {output}"


# -------------------------
# Domain visualization (HTML)
# -------------------------
rule plot_domains:
    input:
        f"results/{GENE}/domains.csv"
    output:
        f"results/{GENE}/domain_plot.html"
    script:
        "scripts/plot_domains.py"