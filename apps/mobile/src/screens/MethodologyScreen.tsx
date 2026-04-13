import { ScrollView, Text } from 'react-native';

export default function MethodologyScreen() {
  return (
    <ScrollView style={{ flex: 1, padding: 12 }}>
      <Text style={{ fontSize: 22, fontWeight: '800' }}>Méthodologie</Text>
      <Text style={{ marginTop: 8 }}>
        Les scores indiquent une aide à la décision basée sur des familles d'ingrédients.
      </Text>
      <Text style={{ marginTop: 8 }}>
        Ce que les scores veulent dire: une estimation heuristique du profil d'une recette.
      </Text>
      <Text style={{ marginTop: 8 }}>
        Ce que les scores ne veulent pas dire: ce n'est pas un test de laboratoire, ni un avis médical.
      </Text>
      <Text style={{ marginTop: 8 }}>
        Les niveaux de contamination varient selon origine, produit, lot et préparation.
      </Text>
      <Text style={{ marginTop: 8 }}>
        La variété alimentaire reste importante.
      </Text>
      <Text style={{ marginTop: 8, fontWeight: '700' }}>
        Important: cette application ne promet aucun effet thérapeutique.
      </Text>
    </ScrollView>
  );
}
