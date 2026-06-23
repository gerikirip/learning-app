import type { Card, CardInput, Deck, DeckDetail, DeckInput, ReviewRating } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000';

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers
    },
    ...options
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(text || `Request failed with ${response.status}`);
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json() as Promise<T>;
}

export const api = {
  health: () => request<{ status: string }>('/health'),
  listDecks: () => request<Deck[]>('/api/decks'),
  getDeck: (deckId: number) => request<DeckDetail>(`/api/decks/${deckId}`),
  createDeck: (payload: DeckInput) => request<Deck>('/api/decks', {
    method: 'POST',
    body: JSON.stringify(payload)
  }),
  createCard: (deckId: number, payload: CardInput) => request<Card>(`/api/decks/${deckId}/cards`, {
    method: 'POST',
    body: JSON.stringify(payload)
  }),
  reviewCard: (cardId: number, rating: ReviewRating) => request(`/api/cards/${cardId}/reviews`, {
    method: 'POST',
    body: JSON.stringify({ rating })
  })
};
