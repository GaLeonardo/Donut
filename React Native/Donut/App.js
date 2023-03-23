import React, { useRef, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import * as THREE from 'three';
import { Canvas, useFrame } from '@react-three/fiber';
import { Picker } from '@react-native-picker/picker';

const Donut = ({ color }) => {
  const meshRef = useRef();

  useFrame(() => {
    meshRef.current.rotation.x += 0.01;
    meshRef.current.rotation.y += 0.02;
  });

  const donutGeometry = new THREE.TorusGeometry(1, 0.5, 16, 100);
  const donutMaterial = new THREE.MeshBasicMaterial({
    color,
  });

  return (
    <mesh ref={meshRef} geometry={donutGeometry} material={donutMaterial} />
  );
};

const App = () => {
  const [color, setColor] = useState('#ffc107');

  const handleColorChange = (color) => {
    setColor(color);
  };

  return (
    <View style={{ flex: 1 }}>
      <View style={styles.pickerContainer}>
        <Text style={styles.label}>Choose a flavor:</Text>
        <Picker
          style={styles.picker}
          selectedValue={color}
          onValueChange={handleColorChange}
        >
          <Picker.Item label="Chocolate" value="#964b00" />
          <Picker.Item label="Strawberry" value="#ff69b4" />
          <Picker.Item label="Cream" value="#ffc107" />
        </Picker>
      </View>
      <Canvas style={{ flex: 1 }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        <Donut color={color} />
      </Canvas>
    </View>
  );
};

const styles = StyleSheet.create({
  pickerContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#eee',
    padding: 10,
  },
  label: {
    fontSize: 16,
    marginRight: 10,
  },
  picker: {
    flex: 1,
  },
});

export default App;
