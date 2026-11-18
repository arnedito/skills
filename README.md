# skills

*Skills* de [Claude Code](https://claude.com/claude-code) para presentaciones científicas, diagramas y flujo de trabajo en repos.

| Skill | Qué hace |
|---|---|
| [`charlas-charlie`](charlas-charlie) | Estilo y caja de herramientas para charlas en Beamer/LaTeX: 6 temas, portada con logos, fondos *low-poly*, figuras matplotlib con el mismo estilo, scripts para compilar y revisar cada slide |
| [`tikz-charlie`](tikz-charlie) | Criterios estéticos, plantillas y verificación para diagramas TikZ (slides, papers, tesis) |
| [`charlie-brain`](charlie-brain) | Monta y hace evolucionar el cerebro de un repo: `CLAUDE.md` corto, wiki, ADRs, capas de tests, CI y flujo issue → PR (`init`, `audit`, `retro`) |
| [`para-el-carro`](para-el-carro) | Pide al agente que vuelva a explicar lo último despacio y con contexto |

## Instalación

```sh
git clone https://github.com/arnedito/skills.git ~/skills
ln -s ~/skills/charlas-charlie ~/.claude/skills/charlas-charlie
ln -s ~/skills/tikz-charlie ~/.claude/skills/tikz-charlie
ln -s ~/skills/charlie-brain ~/.claude/skills/charlie-brain
ln -s ~/skills/para-el-carro ~/.claude/skills/para-el-carro
```

Los logos institucionales no se distribuyen: ver `charlas-charlie/assets/estilo/logos/LEEME.md`.

`charlie-brain` funciona mejor con las [skills de Matt Pocock](https://github.com/mattpocock/skills) instaladas (`grilling`, `codebase-design`, `tdd`, `retro`, `improve-codebase-architecture`) y con `humanizer`. Su modo `retro` adapta la `retro` de Pocock; la base del `CLAUDE.md` viene de [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills); `para-el-carro` se inspira en `wait-what` de Pocock.

Licencia MIT (cada skill lleva la suya).
