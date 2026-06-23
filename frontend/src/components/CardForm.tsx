import { FormEvent, useState } from 'react';

import type { CardInput, CardType } from '../types';

interface CardFormProps {
  onCreate: (payload: CardInput) => Promise<void>;
}

export function CardForm({ onCreate }: CardFormProps) {
  const [payload, setPayload] = useState<CardInput>({
    front: '',
    back: '',
    card_type: 'concept'
  });

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    if (!payload.front.trim() || !payload.back.trim()) return;
    await onCreate(payload);
    setPayload({ front: '', back: '', card_type: 'concept' });
  }

  return (
    <form className="panel form-grid" onSubmit={handleSubmit}>
      <h3>Add card</h3>
      <select
        value={payload.card_type}
        onChange={(event) => setPayload({ ...payload, card_type: event.target.value as CardType })}
      >
        <option value="concept">concept</option>
        <option value="command">command</option>
        <option value="scenario">scenario</option>
        <option value="interview">interview</option>
        <option value="lab">lab</option>
      </select>
      <textarea
        placeholder="Front / question"
        value={payload.front}
        onChange={(event) => setPayload({ ...payload, front: event.target.value })}
      />
      <textarea
        placeholder="Back / answer"
        value={payload.back}
        onChange={(event) => setPayload({ ...payload, back: event.target.value })}
      />
      <button type="submit">Add card</button>
    </form>
  );
}
