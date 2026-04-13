import React, { useEffect, useState } from 'react';
import { FlatList, Pressable, Text, TextInput, View } from 'react-native';
import RecipeCard from '../components/RecipeCard';
import { useAppStore } from '../store/useAppStore';

export default function HomeScreen() {
  const { recipes, favorites, loadInitial, search, searchFromIngredients, toggleFavorite } = useAppStore();
  const [query, setQuery] = useState('');
  const [ingredients, setIngredients] = useState('');

  useEffect(() => {
    loadInitial();
  }, [loadInitial]);

  return (
    <View style={{ flex: 1, padding: 12, backgroundColor: '#f4f6fb' }}>
      <Text style={{ fontSize: 22, fontWeight: '800' }}>Bienvenue</Text>
      <Text style={{ marginBottom: 8 }}>Recettes simples, scores heuristiques, aide à la décision.</Text>

      <TextInput
        placeholder="Rechercher une recette ou ingrédient"
        value={query}
        onChangeText={setQuery}
        style={{ backgroundColor: 'white', borderRadius: 10, padding: 10, marginBottom: 8 }}
      />
      <Pressable onPress={() => search(query)} style={{ padding: 10, backgroundColor: '#1e88e5', borderRadius: 8, marginBottom: 12 }}>
        <Text style={{ color: 'white', textAlign: 'center' }}>Rechercher</Text>
      </Pressable>

      <TextInput
        placeholder="Mes ingrédients (ex: oeuf,tomate,oignon)"
        value={ingredients}
        onChangeText={setIngredients}
        style={{ backgroundColor: 'white', borderRadius: 10, padding: 10, marginBottom: 8 }}
      />
      <Pressable
        onPress={() => searchFromIngredients(ingredients.split(',').map((x) => x.trim()).filter(Boolean))}
        style={{ padding: 10, backgroundColor: '#43a047', borderRadius: 8, marginBottom: 12 }}
      >
        <Text style={{ color: 'white', textAlign: 'center' }}>Recettes avec mes ingrédients</Text>
      </Pressable>

      {recipes.length === 0 ? (
        <Text>Aucune recette pour le moment. Essayez une recherche différente.</Text>
      ) : (
        <FlatList
          data={recipes}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <RecipeCard
              recipe={item}
              isFavorite={favorites.includes(item.id)}
              onToggleFavorite={() => toggleFavorite(item.id)}
            />
          )}
        />
      )}
    </View>
  );
}
