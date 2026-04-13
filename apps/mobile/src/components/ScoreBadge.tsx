import React from 'react';
import { Text, View } from 'react-native';

type Props = { title: string; score: number; label: string };

export default function ScoreBadge({ title, score, label }: Props) {
  return (
    <View style={{ padding: 8, borderRadius: 8, backgroundColor: '#eef3ff', marginTop: 6 }}>
      <Text style={{ fontWeight: '700' }}>{title}</Text>
      <Text>{score}/100 — {label}</Text>
    </View>
  );
}
