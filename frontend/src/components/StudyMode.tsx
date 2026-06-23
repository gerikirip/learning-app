import { useMemo, useState } from 'react';

import type { Card, ReviewRating } from '../types';

interface StudyModeProps {
  cards: Card[];
  onReview: (cardId: number, rating: ReviewRating) => Promise<void>;
}

export function StudyMode({ cards, onReview }: StudyModeProps) {
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);

  const orderedCards = useMemo(() => {
    const priority = { again: 0, new: 1, good: 2, easy: 3 };
    return [...cards].sort((a, b) => priority[a.difficulty] - priority[b.difficulty]);
  }, [cards]);

  if (orderedCards.length === 0) {
    return <div className="panel empty">No cards yet. Add one to start studying.</div>;
  }

  const current = orderedCards[index % orderedCards.length];

  async function rate(rating: ReviewRating) {
    await onReview(current.id, rating);
    setRevealed(false);
    setIndex((value) => (value + 1) % orderedCards.length);
  }

  return (
    <section className="panel study-card">
      <div className="study-meta">
        <span>{current.card_type}</span>
        <span>Difficulty: {current.difficulty}</span>
        <span>{index + 1} / {orderedCards.length}</span>
      </div>

      <div className="flashcard">
        <p className="label">Front</p>
        <h2>{current.front}</h2>
        {revealed ? (
          <>
            <p className="label">Back</p>
            <p className="answer">{current.back}</p>
          </>
        ) : (
          <button onClick={() => setRevealed(true)}>Reveal answer</button>
        )}
      </div>

      {revealed && (
        <div className="rating-row">
          <button className="again" onClick={() => rate('again')}>Again</button>
          <button className="good" onClick={() => rate('good')}>Good</button>
          <button className="easy" onClick={() => rate('easy')}>Easy</button>
        </div>
      )}
    </section>
  );
}
