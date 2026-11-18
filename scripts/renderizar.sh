#!/bin/sh
# renderizar.sh [main.pdf] [dpi] [primera] [última]: una PNG por página en render/<base>-NN.png, para mirarlas.
set -eu
pdf=${1:-main.pdf}; dpi=${2:-80}
dir=$(cd "$(dirname "$pdf")" && pwd); base=$(basename "$pdf" .pdf)
mkdir -p "$dir/render"
rm -f "$dir/render/$base"-*.png
if [ $# -ge 4 ]; then rango="-f $3 -l $4"; else rango=""; fi
# shellcheck disable=SC2086
pdftoppm -r "$dpi" $rango -png "$dir/$base.pdf" "$dir/render/$base"
ls "$dir/render/$base"-*.png
