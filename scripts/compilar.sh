#!/bin/sh
# compilar.sh [main.tex]: compila con latexmk (pdflatex) y resume lo que hay que mirar en el log:
# errores, cajas que se salen (> 1pt), ficheros que faltan, referencias rotas y avisos de charlas-charlie.
set -u
f=${1:-main.tex}
cd "$(dirname "$f")" || exit 1
base=$(basename "$f" .tex)
latexmk -pdf -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null 2>&1
rc=$?
log=$base.log
if [ $rc -ne 0 ]; then
  echo "ERROR compilando $base.tex (latexmk $rc). Primeras líneas del error:"
  grep -n -A4 '^!' "$log" | head -40
  exit $rc
fi
n=$(pdfinfo "$base.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
echo "OK: $(pwd)/$base.pdf ($n páginas)"
# la línea de un aviso apunta al \end{frame}; para saber la slide, mira la hoja de contactos
grep -E '^Overfull' "$log" | awk '{gsub(/[()pt]/,"",$3); if ($3+0 > 1) print}' | sed 's/^/  ⚠ /' | head -20
grep -E "LaTeX Warning: (Reference|Citation).*undefined|File .* not found|Package charlas-charlie Warning|Font shape .* undefined" "$log" \
  | sort -u | sed 's/^/  ⚠ /' | head -20
exit 0
