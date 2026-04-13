import React from 'react';
import { render } from '@testing-library/react-native';
import MethodologyScreen from '../MethodologyScreen';

describe('MethodologyScreen', () => {
  it('shows non-medical wording', () => {
    const { getByText } = render(<MethodologyScreen />);
    expect(getByText(/pas un test de laboratoire/i)).toBeTruthy();
  });
});
