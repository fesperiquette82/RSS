# RSS Monorepo (Recettes & Score Simplifié)

Monorepo MVP avec :
- **mobile** : Expo + React Native + TypeScript
- **backend** : FastAPI + MongoDB

## Prérequis

- Node.js 20+
- Python 3.11+
- Docker + Docker Compose

## Démarrage rapide

### 1) Lancer le backend localement (API + MongoDB)

```bash
docker compose up --build
```

API disponible sur `http://localhost:8000`.

### 2) Lancer l'application mobile

```bash
npm install
npm run mobile:start
```

Pour ouvrir Android en local depuis Expo :

```bash
npm --workspace apps/mobile run android
```

## Build Android via fichier YAML (GitHub Actions)

### Debug APK

Le fichier `.github/workflows/android-build.yml` construit un **APK Android (profil EAS preview)** automatiquement :

- au `push` sur `main`
- sur chaque `pull_request`
- manuellement via `workflow_dispatch`

Le workflow :
1. installe Node.js,
2. installe les dépendances mobile,
3. lance `eas build` avec le profil `preview`,
4. télécharge l'APK généré,
5. publie l'artefact `rss-mobile-debug-apk`.

### Release AAB (Play Console)

Le fichier `.github/workflows/android-release.yml` construit un **AAB release** à la demande (`workflow_dispatch`) via **EAS Build** et publie l’artefact `rss-mobile-release-aab`.

Pré-requis GitHub :
- définir le secret repository `EXPO_TOKEN` (token Expo/EAS avec droits de build)

Le secret `EXPO_TOKEN` est requis pour les workflows debug et release.

Si `EXPO_TOKEN` est absent, les workflows Android passent en mode *skip* (warning) au lieu d'échouer.

Pré-requis Expo :
- projet Expo/EAS initialisé pour l'app mobile
- credentials Android configurés dans Expo pour signer le build release

## Tests

### Backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r apps/api/requirements.txt
pytest apps/api/tests
```

### Mobile

```bash
npm --workspace apps/mobile run test
```

## Seed de données recettes

```bash
python -m apps.api.app.seed
```
