import { create } from 'zustand';
import { api } from '../api/client';
import { Recipe } from '../types';

type State = {
  recipes: Recipe[];
  favorites: string[];
  shoppingList: string[];
  loading: boolean;
  loadInitial: () => Promise<void>;
  search: (q: string) => Promise<void>;
  searchFromIngredients: (ingredients: string[]) => Promise<void>;
  toggleFavorite: (id: string) => Promise<void>;
  addShoppingItem: (item: string) => Promise<void>;
  removeShoppingItem: (item: string) => Promise<void>;
};

export const useAppStore = create<State>((set, get) => ({
  recipes: [],
  favorites: [],
  shoppingList: [],
  loading: false,

  loadInitial: async () => {
    set({ loading: true });
    const [recipes, favorites, shopping] = await Promise.all([
      api.listRecipes(),
      api.getFavorites(),
      api.getShoppingList()
    ]);
    set({ recipes: recipes.items, favorites: favorites.recipe_ids, shoppingList: shopping.items, loading: false });
  },

  search: async (q) => {
    const recipes = await api.listRecipes(q);
    set({ recipes: recipes.items });
  },

  searchFromIngredients: async (ingredients) => {
    const recipes = await api.searchByIngredients(ingredients);
    set({ recipes: recipes.items });
  },

  toggleFavorite: async (id) => {
    const isFav = get().favorites.includes(id);
    const next = await api.toggleFavorite(id, isFav);
    set({ favorites: next.recipe_ids });
  },

  addShoppingItem: async (item) => {
    if (!item.trim()) return;
    const next = await api.addShoppingItem(item);
    set({ shoppingList: next.items });
  },

  removeShoppingItem: async (item) => {
    const next = await api.removeShoppingItem(item);
    set({ shoppingList: next.items });
  }
}));
