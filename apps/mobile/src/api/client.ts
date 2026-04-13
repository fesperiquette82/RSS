import { Recipe } from '../types';

const API_URL = process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8000';

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: { 'Content-Type': 'application/json', ...(init?.headers || {}) }
  });
  if (!res.ok) throw new Error(`Erreur API ${res.status}`);
  return res.json() as Promise<T>;
}

export const api = {
  listRecipes: (q = '') =>
    request<{ items: Recipe[]; total: number }>(`/api/v1/recipes${q ? `?q=${encodeURIComponent(q)}` : ''}`),
  searchByIngredients: (ingredients: string[]) =>
    request<{ items: Recipe[]; total: number }>('/api/v1/recipes/search-by-ingredients', {
      method: 'POST',
      body: JSON.stringify({ ingredients, match_all: false })
    }),
  getFavorites: () => request<{ recipe_ids: string[] }>('/api/v1/favorites'),
  toggleFavorite: (id: string, active: boolean) =>
    request<{ recipe_ids: string[] }>(`/api/v1/favorites/${id}`, { method: active ? 'DELETE' : 'POST' }),
  getShoppingList: () => request<{ items: string[] }>('/api/v1/shopping-list'),
  addShoppingItem: (item: string) =>
    request<{ items: string[] }>('/api/v1/shopping-list/items', {
      method: 'POST',
      body: JSON.stringify({ item })
    }),
  removeShoppingItem: (item: string) => request<{ items: string[] }>(`/api/v1/shopping-list/items/${encodeURIComponent(item)}`, { method: 'DELETE' })
};
