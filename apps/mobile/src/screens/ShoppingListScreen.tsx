import React, { useState } from 'react';
import { Pressable, Text, TextInput, View } from 'react-native';
import { useAppStore } from '../store/useAppStore';

export default function ShoppingListScreen() {
  const { shoppingList, addShoppingItem, removeShoppingItem } = useAppStore();
  const [item, setItem] = useState('');

  return (
    <View style={{ flex: 1, padding: 12 }}>
      <Text style={{ fontSize: 22, fontWeight: '700' }}>Liste de courses</Text>
      <TextInput value={item} onChangeText={setItem} placeholder="Ajouter un article" style={{ borderWidth: 1, borderColor: '#ddd', borderRadius: 8, padding: 8, marginVertical: 8 }} />
      <Pressable onPress={() => { addShoppingItem(item); setItem(''); }} style={{ backgroundColor: '#1e88e5', padding: 10, borderRadius: 8 }}>
        <Text style={{ color: 'white', textAlign: 'center' }}>Ajouter</Text>
      </Pressable>

      {shoppingList.length === 0 ? (
        <Text style={{ marginTop: 12 }}>Votre liste est vide.</Text>
      ) : (
        <View style={{ marginTop: 12 }}>
          {shoppingList.map((x) => (
            <Pressable key={x} onPress={() => removeShoppingItem(x)}>
              <Text>• {x} (toucher pour retirer)</Text>
            </Pressable>
          ))}
        </View>
      )}
    </View>
  );
}
