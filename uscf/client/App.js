import { StatusBar } from 'expo-status-bar';
import { StyleSheet, View } from 'react-native';
import Lookup from './components/player_lookup/lookup';
import Home from './components/home/home';
import Foot from './components/navbar/foot';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();
export default function App(){
  return (
    <NavigationContainer>
      
      <Stack.Navigator
        screenOptions={{
          headerStyle:{
            backgroundColor:"#01012b"
          },
          headerTintColor:"#fff"
        }} >
        
        <Stack.Screen 
          name="Home" 
          component={Home}/>
 
        <Stack.Screen 
          name="Lookup" 
          component={Lookup} />
        
      </Stack.Navigator>
      <Foot />
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inp:{
    borderWidth: 1,
    borderColor: '#777',
    padding: 8,
    margin: 10,
    width: 200,
  }
});
