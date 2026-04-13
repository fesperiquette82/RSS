<<<<<<< codex/build-full-stack-recipe-application
# Repository Agent Instructions

- Scope: entire repository.
- Keep implementation simple, readable, and production-minded.
- Use French copy for user-facing mobile UI by default.
- Never use medical claims; use decision-support and heuristic wording.
- Prefer deterministic local-first workflows and clear README commands.
=======
# AGENTS.md

## Repository expectations
- Build a full-stack MVP for a recipe mobile app.
- Prioritize clarity, simplicity, and runnable code.
- Do not leave placeholder TODOs when a working implementation is possible.
- Keep the architecture simple and monorepo-based.

## Product rules
- Never claim "cadmium-free", "detox", or medical benefits.
- Use non-medical wording:
  - low probable cadmium exposure
  - anti-inflammatory profile
  - heuristic score
  - decision support
- French UI by default.

## Tech rules
- Frontend: Expo + React Native + TypeScript
- Backend: FastAPI + Python
- Database: MongoDB
- Use clean folder structure and modular code.
- Add seed data and a clear README.

## Quality rules
- Add linting and formatting.
- Add basic tests.
- Add Docker Compose for local backend development.
- Prefer robust simple solutions over complex abstractions.

## Delivery rules
- At the end of each major task, update README if needed.
- Ensure the project runs locally with explicit commands.
- Explain assumptions briefly.
>>>>>>> main
