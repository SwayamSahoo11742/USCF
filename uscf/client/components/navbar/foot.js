import React from 'react';
import { StyleSheet, View, Text, Image } from 'react-native';

export default function Foot({ navigation }) {
  return (
    <View style={styles.container}>
      <View style={styles.navContainer}>
        <Image source={require('./chesscomLogo.png')} style={styles.icon}/>
        <Image source={require('./lichessLogo.png')} style={styles.icon}/>
        <Image source={require('./USCFLogo.png')} style={styles.icon}/>
        <Image source={require('./newsIcon.png')} style={styles.icon}/>
        <Image source={require('./profileIcon.png')} style={styles.icon}/>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#01012b',
    alignItems: 'center',
    padding: 20,
    height: 75,
  },
  navContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between', 
  },
  icon: {
    height:30,
    width:30,
    marginRight:15,
    marginLeft:15,
  },
});
