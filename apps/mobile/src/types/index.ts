export type Score = {
  score: number;
  label: string;
  reasons: string[];
  methodology_note: string;
};

export type Recipe = {
  id: string;
  title: string;
  description: string;
  category: string;
  duration_minutes: number;
  ingredients: string[];
  steps: string[];
  cadmium_profile: Score;
  anti_inflammatory_profile: Score;
};
