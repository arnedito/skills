#!/bin/sh
# hoja_contactos.sh [main.pdf] [columnas] [dpi]: todas las slides en una sola imagen numerada
# (<base>-hoja.png junto al PDF). Sirve para ver de un vistazo el ritmo, la jerarquía y lo que desentona.
set -eu
pdf=${1:-main.pdf}; cols=${2:-4}; dpi=${3:-90}
dir=$(cd "$(dirname "$pdf")" && pwd); base=$(basename "$pdf" .pdf)
n=$(pdfinfo "$dir/$base.pdf" | awk '/^Pages/{print $2}')
filas=$(( (n + cols - 1) / cols ))
tmp=$(mktemp -d)
cat > "$tmp/hoja.tex" <<TEX
\documentclass{article}
\usepackage[paperwidth=$(( cols * 8 + 1 ))cm,paperheight=$(( filas * 5 + 1 ))cm,margin=0.5cm]{geometry}
\usepackage{graphicx,pgffor,xcolor}\pagestyle{empty}\setlength\parindent{0pt}\setlength\fboxsep{0pt}
\begin{document}\centering
\foreach \p in {1,...,$n}{\begin{minipage}[t]{7.8cm}\centering
  \fcolorbox{black!25}{white}{\includegraphics[page=\p,width=7.5cm]{$dir/$base.pdf}}\par
  {\scriptsize\sffamily\p}\end{minipage}\ifnum\numexpr\p-($cols*(\p/$cols))\relax=0\par\vspace{2pt}\fi}
\end{document}
TEX
(cd "$tmp" && pdflatex -interaction=nonstopmode hoja.tex >/dev/null 2>&1) || { echo "fallo la hoja"; exit 1; }
pdftoppm -r "$dpi" -singlefile -png "$tmp/hoja.pdf" "$dir/$base-hoja"
rm -rf "$tmp"
echo "$dir/$base-hoja.png ($n slides)"
