import { FormEvent, useState } from 'react';

import type { DeckInput } from '../types';

interface DeckFormProps {
  onCreate: (payload: DeckInput) => Promise<void>;
}

export function DeckForm({ onCreate }: DeckFormProps) {
  const [payload, setPayload] = useState<DeckInput>({
    title: '',
    description: '',
    topic: 'custom',
    level: 'beginner'
  });

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    if (!payload.title.trim()) return;
    await onCreate(payload);
    setPayload({ title: '', description: '', topic: 'custom', level: 'beginner' });
  }

  return (
    <form className="panel form-grid" onSubmit={handleSubmit}>
      <h3>Create deck</h3>
      <input
        placeholder="Deck title"
        value={payload.title}
        onChange={(event) => setPayload({ ...payload, title: event.target.value })}
      />
      <input
        placeholder="Topic, e.g. kubernetes"
        value={payload.topic}
        onChange={(event) => setPayload({ ...payload, topic: event.target.value })}
      />
      <select
        value={payload.level}
        onChange={(event) => setPayload({ ...payload, level: event.target.value })}
      >
        <option value="beginner">beginner</option>
        <option value="intermediate">intermediate</option>
        <option value="advanced">advanced</option>
      </select>
      <textarea
        placeholder="Description"
        value={payload.description}
        onChange={(event) => setPayload({ ...payload, description: event.target.value })}
      />
      <button type="submit">Add deck</button>
    </form>
  );
}
