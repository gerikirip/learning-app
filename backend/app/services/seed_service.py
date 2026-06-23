from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Card, Deck
from app.seed.devops_decks import DEVOPS_DECKS


def seed_devops_content(db: Session) -> None:
    existing = db.scalar(select(Deck).limit(1))
    if existing is not None:
        return

    for deck_data in DEVOPS_DECKS:
        deck_payload = dict(deck_data)
        cards = deck_payload.pop("cards")
        deck = Deck(**deck_payload)
        db.add(deck)
        db.flush()
        for card_data in cards:
            db.add(Card(deck_id=deck.id, **card_data))

    db.commit()
