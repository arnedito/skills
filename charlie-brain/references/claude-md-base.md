# Base del CLAUDE.md (principios de Karpathy)

Punto de partida para la entrevista de `init`. Cada principio se discute: se queda, se ajusta al proyecto o se quita. Si el `~/.claude/CLAUDE.md` global ya los lleva, el `CLAUDE.md` del repo no los repite: se pagan en cada turno.

Fuente: forrestchang/andrej-karpathy-skills (MIT), basado en las observaciones de Andrej Karpathy sobre errores típicos de los LLM al programar.

```markdown
Bias toward caution over speed; for trivial tasks, use judgment.

1. **Think before coding.** State assumptions. If several interpretations exist, present them, don't pick silently. If a simpler approach exists, say so. If something is unclear, stop and ask.
2. **Simplicity first.** Minimum code that solves the problem. No speculative features, single-use abstractions, unrequested configurability or handling of impossible errors. If 200 lines could be 50, rewrite.
3. **Surgical changes.** Touch only what the request needs. Don't improve adjacent code, comments or formatting; match existing style. Mention unrelated dead code, don't delete it. Remove only the orphans your own change created.
4. **Goal-driven execution.** Turn tasks into verifiable goals (test that reproduces → make it pass). For multi-step tasks, state a brief plan: `step → verify: check`. Loop until verified.
```

## Qué suele ajustarse

- **Prototipo o exploración**: el 1 y el 4 se relajan ("pregunta solo si bloquea").
- **Código científico**: el 4 se refuerza: cada ecuación implementada tiene su test que cita la ecuación del paper.
- **Refactor planificado** (tras un `audit`): el 3 se suspende para el alcance del issue, no más.
- **Repo con mucho código heredado**: el 3 pesa más; añade "lee el módulo antes de tocarlo".
