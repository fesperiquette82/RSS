import { Pressable, Text, View } from 'react-native';
import { Recipe } from '../types';
import ScoreBadge from './ScoreBadge';

type Props = { recipe: Recipe; isFavorite: boolean; onToggleFavorite: () => void };

export default function RecipeCard({ recipe, isFavorite, onToggleFavorite }: Props) {
  return (
    <View style={{ backgroundColor: 'white', padding: 12, borderRadius: 12, marginBottom: 12 }}>
      <Text style={{ fontSize: 18, fontWeight: '700' }}>{recipe.title}</Text>
      <Text style={{ color: '#555' }}>{recipe.description}</Text>
      <Text style={{ marginTop: 6 }}>{recipe.duration_minutes} min • {recipe.category}</Text>
      <ScoreBadge title="Faible exposition probable au cadmium" score={recipe.cadmium_profile.score} label={recipe.cadmium_profile.label} />
      <ScoreBadge title="Profil anti-inflammatoire" score={recipe.anti_inflammatory_profile.score} label={recipe.anti_inflammatory_profile.label} />
      <Pressable onPress={onToggleFavorite} style={{ marginTop: 8 }}>
        <Text style={{ color: '#1b5e20' }}>{isFavorite ? '★ Retirer des favoris' : '☆ Ajouter aux favoris'}</Text>
      </Pressable>
    </View>
  );
}
