# skills

*Skills* de [Claude Code](https://claude.com/claude-code) para presentaciones científicas y diagramas.

| Skill | Qué hace |
|---|---|
| [`charlas-charlie`](charlas-charlie) | Estilo y caja de herramientas para charlas en Beamer/LaTeX: 6 temas, portada con logos, fondos *low-poly*, figuras matplotlib con el mismo estilo, scripts para compilar y revisar cada slide |
| [`tikz-charlie`](tikz-charlie) | Criterios estéticos, plantillas y verificación para diagramas TikZ (slides, papers, tesis) |

## Instalación

```sh
git clone https://github.com/arnedito/skills.git ~/skills
ln -s ~/skills/charlas-charlie ~/.claude/skills/charlas-charlie
ln -s ~/skills/tikz-charlie ~/.claude/skills/tikz-charlie
```

Los logos institucionales no se distribuyen: ver `charlas-charlie/assets/estilo/logos/LEEME.md`.

Licencia MIT (cada skill lleva la suya).
