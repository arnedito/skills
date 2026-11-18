#!/bin/sh
# nueva_charla.sh <carpeta> [--tema bloques] [--idioma english] [--titulo "..."]
# Monta una charla nueva: main.tex con portada y logos, estilo/ copiado (versión anotada), figs/,
# diagramas/, make_figs.py de plantilla y BRIEF.md para las decisiones. No pisa una carpeta que exista.
set -eu
SKILL=$(cd "$(dirname "$0")/.." && pwd)
[ $# -ge 1 ] || { echo "uso: nueva_charla.sh <carpeta> [--tema T] [--idioma I] [--titulo \"...\"]"; exit 1; }
dest=$1; shift
tema=bloques; idioma=english; titulo="Título: el mensaje de la charla"
while [ $# -gt 0 ]; do
  case $1 in
    --tema) tema=$2; shift 2;;
    --idioma) idioma=$2; shift 2;;
    --titulo) titulo=$2; shift 2;;
    *) echo "opción desconocida: $1"; exit 1;;
  esac
done
[ -f "$SKILL/assets/estilo/tema-$tema.tex" ] || { echo "tema desconocido: $tema"; exit 1; }
[ -e "$dest" ] && { echo "ya existe: $dest (no la toco)"; exit 1; }
version=$(sed -n 's/^\\def\\estiloversion{\(.*\)}/\1/p' "$SKILL/assets/estilo/preambulo.tex")
if [ "$idioma" = spanish ]; then seccion="Planteamiento"; mensaje="El título es el mensaje"
  cuerpo="Una idea por slide: el título dice el mensaje; el cuerpo lo demuestra."; frase="La frase que cierra el bloque"
else seccion="Motivation"; mensaje="The title states the message"
  cuerpo="One idea per slide: the title states the message; the body proves it."; frase="The sentence that closes the block"; fi
mkdir -p "$dest/figs" "$dest/diagramas"
cp -R "$SKILL/assets/estilo" "$dest/estilo"
rm -f "$dest/estilo/.DS_Store"
: # VERSION ya viene en assets/estilo
nombre="$titulo ($(basename "$dest"))"; fecha=$(date +%Y-%m-%d)
esc() { printf '%s' "$1" | sed 's/[&|\\]/\\&/g'; }
for f in main.tex BRIEF.md; do
  sed -e "s|__NOMBRE__|$(esc "$nombre")|g" -e "s|__FECHA__|$fecha|g" -e "s|__VERSION__|$version|g" \
      -e "s|__TEMA__|$tema|g" -e "s|__IDIOMA__|$idioma|g" -e "s|__TITULO__|$(esc "$titulo")|g" \
      -e "s|__SECCION__|$seccion|g" -e "s|__MENSAJE__|$mensaje|g" -e "s|__CUERPO__|$cuerpo|g" -e "s|__FRASE__|$frase|g" "$SKILL/assets/plantilla/$f" > "$dest/$f"
done
cp "$SKILL/assets/plantilla/make_figs.py" "$dest/"
echo "Charla creada en $dest (tema $tema, idioma $idioma, estilo v$version)"
echo "  compilar:  $SKILL/scripts/compilar.sh $dest/main.tex"
