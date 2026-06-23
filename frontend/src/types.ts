export type Difficulty = 'new' | 'again' | 'good' | 'easy';
export type CardType = 'concept' | 'command' | 'scenario' | 'interview' | 'lab';
export type ReviewRating = 'again' | 'good' | 'easy';

export interface Deck {
  id: number;
  title: string;
  description: string;
  topic: string;
  level: string;
  card_count: number;
  created_at: string;
  updated_at: string;
}

export interface Card {
  id: number;
  deck_id: number;
  front: string;
  back: string;
  card_type: CardType;
  difficulty: Difficulty;
  last_reviewed_at: string | null;
  created_at: string;
  updated_at: string;
}

export interface DeckDetail extends Deck {
  cards: Card[];
}

export interface DeckInput {
  title: string;
  description: string;
  topic: string;
  level: string;
}

export interface CardInput {
  front: string;
  back: string;
  card_type: CardType;
}
