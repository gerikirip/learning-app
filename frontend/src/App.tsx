import { useEffect, useState } from 'react';

import { CardForm } from './components/CardForm';
import { DeckForm } from './components/DeckForm';
import { DeckList } from './components/DeckList';
import { StudyMode } from './components/StudyMode';
import { api } from './services/api';
import type { CardInput, Deck, DeckDetail, DeckInput, ReviewRating } from './types';

function App() {
  const [decks, setDecks] = useState<Deck[]>([]);
  const [selectedDeck, setSelectedDeck] = useState<DeckDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function loadDecks(nextSelectedId?: number) {
    const data = await api.listDecks();
    setDecks(data);
    const targetId = nextSelectedId ?? selectedDeck?.id ?? data[0]?.id;
    if (targetId) {
      await loadDeck(targetId);
    }
  }

  async function loadDeck(deckId: number) {
    const data = await api.getDeck(deckId);
    setSelectedDeck(data);
  }

  useEffect(() => {
    api.health()
      .then(() => loadDecks())
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
    // loadDecks reads selectedDeck once during startup; later calls are explicit.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function createDeck(payload: DeckInput) {
    const deck = await api.createDeck(payload);
    await loadDecks(deck.id);
  }

  async function createCard(payload: CardInput) {
    if (!selectedDeck) return;
    await api.createCard(selectedDeck.id, payload);
    await loadDeck(selectedDeck.id);
    await loadDecks(selectedDeck.id);
  }

  async function reviewCard(cardId: number, rating: ReviewRating) {
    if (!selectedDeck) return;
    await api.reviewCard(cardId, rating);
    await loadDeck(selectedDeck.id);
    await loadDecks(selectedDeck.id);
  }

  if (loading) {
    return <main className="centered">Loading DevOps decks...</main>;
  }

  if (error) {
    return (
      <main className="centered error">
        <h1>Backend unavailable</h1>
        <p>{error}</p>
        <p>Run <code>docker compose up --build</code> from <code>learning-app/</code>.</p>
      </main>
    );
  }

  return (
    <main className="app-shell">
      <header className="hero">
        <div>
          <p className="eyebrow">Docker-first DevOps training</p>
          <h1>DevOps Learning App</h1>
          <p>Flashcards, commands, interview questions, and troubleshooting drills for job readiness.</p>
        </div>
        <div className="hero-card">
          <strong>{decks.length}</strong>
          <span>learning decks</span>
        </div>
      </header>

      <section className="layout">
        <DeckList decks={decks} selectedDeckId={selectedDeck?.id ?? null} onSelect={loadDeck} />

        <div className="content-stack">
          {selectedDeck && (
            <>
              <section className="panel">
                <p className="topic">{selectedDeck.topic}</p>
                <h2>{selectedDeck.title}</h2>
                <p>{selectedDeck.description}</p>
                <p className="muted">{selectedDeck.cards.length} cards · {selectedDeck.level}</p>
              </section>

              <StudyMode cards={selectedDeck.cards} onReview={reviewCard} />

              <section className="card-grid">
                {selectedDeck.cards.map((card) => (
                  <article className="panel mini-card" key={card.id}>
                    <span className={`badge ${card.difficulty}`}>{card.difficulty}</span>
                    <h4>{card.front}</h4>
                    <p>{card.back}</p>
                  </article>
                ))}
              </section>

              <CardForm onCreate={createCard} />
            </>
          )}

          <DeckForm onCreate={createDeck} />
        </div>
      </section>
    </main>
  );
}

export default App;
