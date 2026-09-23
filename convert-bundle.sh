#!/bin/bash
set -euo pipefail

url="https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz"
curl -s "$url" -o lab3-bundle.tar.gz
tar -xzf lab3-bundle.tar.gz
awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv
tr '\t' ',' < cleaned.tsv > cleaned.csv
total=$(wc -l < cleaned.csv | tr -d ' ')
data=$((total -1))
echo "Cleaned data rows remaining: $data"
tar -czf converted-archive.tar.gz cleaned.csv
