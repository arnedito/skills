#!/bin/sh
# comparar_temas.sh main.tex [páginas] [temas...]: compila la charla con cada tema (copia temporal con
# \def\tema cambiado) y junta las primeras páginas en <base>-temas.png, una fila por tema.
# Ej.: comparar_temas.sh main.tex 6            (los 6 temas, 6 primeras páginas)
#      comparar_temas.sh main.tex 4 bloques oscuro
#      DPI=200 comparar_temas.sh main.tex 6      (más resolución, p. ej. para el README)
set -eu
f=$1; paginas=${2:-6}; shift; [ $# -gt 0 ] && shift
temas=${*:-bloques metropolis clasico tufte oscuro editorial}
cd "$(dirname "$f")"; base=$(basename "$f" .tex)
filas=""
for t in $temas; do
  sed "s/\\\\def\\\\tema{[^}]*}/\\\\def\\\\tema{$t}/" "$base.tex" > "$base-tema-$t.tex"
  latexmk -pdf -interaction=nonstopmode -halt-on-error "$base-tema-$t.tex" >/dev/null 2>&1 || echo "  ✗ $t no compila"
  filas="$filas $t"
done
tmp=$(mktemp -d); here=$(pwd)
{
  printf '%s\n' '\documentclass{article}\usepackage[paperwidth='"$(( paginas * 6 + 4 ))"'cm,paperheight='"$(( $(echo $temas | wc -w) * 4 + 1 ))"'cm,margin=0.4cm]{geometry}'
  printf '%s\n' '\usepackage{graphicx}\pagestyle{empty}\setlength\parindent{0pt}\begin{document}'
  for t in $filas; do
    [ -f "$here/$base-tema-$t.pdf" ] || continue
    np=$(pdfinfo "$here/$base-tema-$t.pdf" | awk '/^Pages/{print $2}'); m=$(( np < paginas ? np : paginas ))
    printf '\\makebox[2.8cm][l]{\\small\\sffamily %s}' "$t"
    i=1; while [ $i -le $m ]; do printf '\\fbox{\\includegraphics[page=%d,width=5.6cm]{%s}}\\,' $i "$here/$base-tema-$t.pdf"; i=$((i+1)); done
    printf '%s\n' '\par\vspace{1mm}'
  done
  printf '%s\n' '\end{document}'
} > "$tmp/temas.tex"
(cd "$tmp" && pdflatex -interaction=nonstopmode temas.tex >/dev/null 2>&1) || { echo "fallo la hoja: $tmp/temas.log"; exit 1; }
pdftoppm -r "${DPI:-80}" -singlefile -png "$tmp/temas.pdf" "$here/$base-temas"
rm -rf "$tmp"
for t in $filas; do latexmk -c "$base-tema-$t.tex" >/dev/null 2>&1; rm -f "$base-tema-$t.tex"; done
echo "$here/$base-temas.png (PDF por tema: $base-tema-<tema>.pdf)"
