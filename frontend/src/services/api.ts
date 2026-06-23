import type { Card, CardInput, Deck, DeckDetail, DeckInput, ReviewRating } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? '';
const REQUEST_TIMEOUT_MS = 15000;

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const controller = new AbortController();
  const timeoutId = window.setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);

  try {
    const response = await fetch(`${API_BASE_URL}${path}`, {
      ...options,
      signal: controller.signal,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      }
    });

    if (!response.ok) {
      const text = await response.text();
      throw new Error(text || `Request failed with ${response.status}`);
    }

    if (response.status === 204) {
      return undefined as T;
    }

    return response.json() as Promise<T>;
  } catch (error) {
    if (error instanceof DOMException && error.name === 'AbortError') {
      throw new Error('Backend request timed out. Check BACKEND_URL on the frontend Railway service.');
    }
    throw error;
  } finally {
    window.clearTimeout(timeoutId);
  }
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
