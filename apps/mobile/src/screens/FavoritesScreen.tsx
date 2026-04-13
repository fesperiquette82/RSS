import { Text, View } from 'react-native';
import { useAppStore } from '../store/useAppStore';

export default function FavoritesScreen() {
  const { recipes, favorites } = useAppStore();
  const favoriteRecipes = recipes.filter((r) => favorites.includes(r.id));

  return (
    <View style={{ flex: 1, padding: 12 }}>
      <Text style={{ fontSize: 22, fontWeight: '700' }}>Mes favoris</Text>
      {favoriteRecipes.length === 0 ? (
        <Text>Pas encore de favoris.</Text>
      ) : (
        favoriteRecipes.map((r) => <Text key={r.id}>• {r.title}</Text>)
      )}
    </View>
  );
}
