# Contributing

Every change goes through the same path:

1. Open an issue that says what's wrong or missing and how we'll know it's done.
2. Branch from `main` (`<type>/<issue>-<short-name>`, e.g. `fix/42-carina-labels`).
3. Write a failing test first, then the code that makes it pass.
4. Open a PR that closes the issue. Keep it to one idea and roughly 400 lines; refactors and features go in separate PRs.
5. CI has to pass. A maintainer reviews and merges.

If your change alters how a module works, update its page in `docs/wiki/` and add a line to `docs/wiki/log.md` in the same PR. If it settles a design question, write an ADR in `docs/adr/`.

## Running the checks locally

<build and test commands for this repo>
