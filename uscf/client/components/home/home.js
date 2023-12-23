import { StatusBar } from 'expo-status-bar';
import { StyleSheet, View, Text, TextInput } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack'

export default function Home({navigation}) {
  return (
    <View style={styles.container}>
      <Text>HEY</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#02033d',
    alignItems: 'center',
    justifyContent: 'center',
  }
});
