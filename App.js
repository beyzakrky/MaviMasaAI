import { useEffect, useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { StatusBar } from 'expo-status-bar';
import { Text } from 'react-native';

import SikayetlerScreen from './src/screens/SikayetlerScreen';
// HaritaScreen importu geçici olarak kaldırıldı
import SikayetGirScreen from './src/screens/SikayetGirScreen';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <StatusBar style="light" />
      <Tab.Navigator
        screenOptions={{
          tabBarStyle: {
            backgroundColor: '#1a1a2e',
            borderTopColor: '#16213e',
          },
          tabBarActiveTintColor: '#4CAF50',
          tabBarInactiveTintColor: '#888',
          headerStyle: { backgroundColor: '#1a1a2e' },
          headerTintColor: '#fff',
        }}
      >
        <Tab.Screen
          name="Şikayetler"
          component={SikayetlerScreen}
          options={{ tabBarIcon: () => <Text style={{ fontSize: 20 }}>📋</Text> }}
        />
        
        {/* Harita sekmesi web demosu için gizlendi */}

        <Tab.Screen
          name="Şikayet Gir"
          component={SikayetGirScreen}
          options={{ tabBarIcon: () => <Text style={{ fontSize: 20 }}>➕</Text> }}
        />
      </Tab.Navigator>
    </NavigationContainer>
  );
}