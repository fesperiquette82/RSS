import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import HomeScreen from './src/screens/HomeScreen';
import FavoritesScreen from './src/screens/FavoritesScreen';
import ShoppingListScreen from './src/screens/ShoppingListScreen';
import MethodologyScreen from './src/screens/MethodologyScreen';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <SafeAreaProvider>
      <NavigationContainer>
        <Tab.Navigator screenOptions={{ headerShown: true }}>
          <Tab.Screen name="Accueil" component={HomeScreen} />
          <Tab.Screen name="Favoris" component={FavoritesScreen} />
          <Tab.Screen name="Courses" component={ShoppingListScreen} />
          <Tab.Screen name="Méthodo" component={MethodologyScreen} />
        </Tab.Navigator>
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
