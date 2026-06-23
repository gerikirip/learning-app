import type { Deck } from '../types';

interface DeckListProps {
  decks: Deck[];
  selectedDeckId: number | null;
  onSelect: (deckId: number) => void;
}

export function DeckList({ decks, selectedDeckId, onSelect }: DeckListProps) {
  return (
    <aside className="panel deck-list">
      <h2>DevOps Decks</h2>
      <p className="muted">Choose a topic and practice active recall.</p>
      <div className="deck-stack">
        {decks.map((deck) => (
          <button
            key={deck.id}
            className={`deck-button ${selectedDeckId === deck.id ? 'active' : ''}`}
            onClick={() => onSelect(deck.id)}
          >
            <span className="topic">{deck.topic}</span>
            <strong>{deck.title}</strong>
            <small>{deck.card_count} cards · {deck.level}</small>
          </button>
        ))}
      </div>
    </aside>
  );
}
