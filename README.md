# RSS Monorepo — Recettes Simples & Scores Heuristiques

Application full-stack mobile-first (Expo + FastAPI + MongoDB) orientée recettes simples avec:
- score de **faible exposition probable au cadmium**
- score de **profil anti-inflammatoire**
- recherche et filtres de recettes
- favoris
- liste de courses
- mode « recettes avec mes ingrédients »
- écran méthodologie explicite et non médical

## Structure

- `apps/mobile` — App Expo React Native TypeScript
- `apps/api` — API FastAPI Python
- `seeds/recipes.json` — Données seed (30+ recettes)
- `docs/methodology.md` — Méthodologie scoring
- `docker-compose.yml` — MongoDB + API locale

## Prérequis

- Node.js 20+
- npm 10+
- Python 3.11+
- Docker & Docker Compose

## Variables d'environnement

### API
Copier `apps/api/.env.example` vers `apps/api/.env`.

### Mobile
Copier `apps/mobile/.env.example` vers `apps/mobile/.env`.

## Lancer localement

### Option 1 (recommandée): Docker Compose (API + Mongo)

```bash
make up
```

Puis seed:

```bash
make seed
```

### Mobile

```bash
cd apps/mobile
npm install
npm run start
```

Par défaut, l'app lit `EXPO_PUBLIC_API_URL`.
Sur Android emulator: `http://10.0.2.2:8000`.
Sur iOS simulator: `http://localhost:8000`.

## Développement API sans Docker

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Seed:

```bash
python -m app.seed
```

## Tests

API:
```bash
make test-api
```

Mobile:
```bash
make test-mobile
```

## Lint / format

```bash
make lint
make format
```

## Endpoints clés

- `GET /health`
- `GET /api/v1/recipes`
- `GET /api/v1/recipes/{id}`
- `POST /api/v1/recipes/search-by-ingredients`
- `GET /api/v1/ingredients/search?q=`
- `GET /api/v1/favorites`
- `POST /api/v1/favorites/{recipe_id}`
- `DELETE /api/v1/favorites/{recipe_id}`
- `GET /api/v1/shopping-list`
- `POST /api/v1/shopping-list/items`
- `DELETE /api/v1/shopping-list/items/{name}`
- `GET /api/v1/preferences`
- `PUT /api/v1/preferences`

## Note importante

Cette application fournit une **aide à la décision** basée sur des **scores heuristiques** de familles d'ingrédients et de modes de préparation. Ce n'est pas un avis médical.
