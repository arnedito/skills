#!/bin/sh
# diagrama.sh fichero.tex [tema|fijo] [preambulo-extra.tex]: compila un diagrama suelto y lo deja en
# <fichero>[-<tema>].pdf y .png (200 dpi) junto al fichero (con el tema en el nombre si no es "fijo"), para mirarlo sin compilar la charla entera.
#   tema = bloques | clasico | oscuro | ... : dentro de una slide con ese tema de charlas-charlie
#          (busca charlas-charlie junto a esta skill o en ~/.claude/skills).
#   fijo  (por defecto): standalone sobre blanco con assets/colores-fijos.tex (papers, tesis).
#   preambulo-extra: un .tex con macros que el diagrama necesita (p. ej. \input{selector.tex}).
# TAM=11pt diagrama.sh …: tamaño de letra del documento en modo fijo (por defecto 10pt).
set -eu
f=$1; tema=${2:-fijo}; extra=${3:-}
SKILL=$(cd "$(dirname "$0")/.." && pwd)
dir=$(cd "$(dirname "$f")" && pwd); base=$(basename "$f" .tex)
tmp=$(mktemp -d)
ext=""; [ -n "$extra" ] && ext="\\input{$(cd "$(dirname "$extra")" && pwd)/$(basename "$extra")}"
if [ "$tema" = fijo ]; then
  cat > "$tmp/d.tex" <<TEX
\documentclass[border=4pt,${TAM:-10pt}]{standalone}
\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}\usepackage{amsmath,amssymb,graphicx}
\usepackage[sc]{mathpazo}\usepackage{tikz}
\makeatletter\def\input@path{{$dir/}{$SKILL/assets/}{$SKILL/assets/plantillas/}}\makeatother
\input{colores-fijos}$ext
\begin{document}\input{$dir/$base.tex}\end{document}
TEX
else
  CC=""
  for c in "$SKILL/../charlas-charlie" "$HOME/.claude/skills/charlas-charlie"; do
    [ -f "$c/assets/estilo/preambulo.tex" ] && { CC=$(cd "$c" && pwd); break; }; done
  [ -n "$CC" ] || { echo "no encuentro charlas-charlie para el tema $tema; usa 'fijo'"; exit 1; }
  cat > "$tmp/d.tex" <<TEX
\documentclass[aspectratio=169,11pt]{beamer}
\def\tema{$tema}\def\logos{}\def\estilodir{$CC/assets/estilo/}
\makeatletter\def\input@path{{$dir/}{$CC/assets/estilo/}{$SKILL/assets/plantillas/}}\makeatother
\input{preambulo}$ext
\begin{document}\begin{frame}[plain]\centering\input{$dir/$base.tex}\end{frame}\end{document}
TEX
fi
if ! (cd "$tmp" && pdflatex -interaction=nonstopmode -halt-on-error d.tex >/dev/null 2>&1); then
  echo "ERROR compilando $base.tex:"; grep -A4 '^!' "$tmp/d.log" | head -20; rm -rf "$tmp"; exit 1; fi
grep -E '^Overfull' "$tmp/d.log" | sed 's/^/  ⚠ más ancho que la slide (o texto que se sale de una caja): /' | head -5 || true
out=$base; [ "$tema" = fijo ] || out=$base-$tema
cp "$tmp/d.pdf" "$dir/$out.pdf"
pdftoppm -r 200 -singlefile -png "$dir/$out.pdf" "$dir/$out"
rm -rf "$tmp"
echo "$dir/$out.png"
