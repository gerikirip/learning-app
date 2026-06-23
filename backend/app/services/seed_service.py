from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models import Card, Deck
from app.seed.devops_decks import DEVOPS_DECKS


def seed_devops_content(db: Session) -> dict[str, int | bool]:
    deck_count = db.scalar(select(func.count()).select_from(Deck)) or 0
    if deck_count > 0:
        card_count = db.scalar(select(func.count()).select_from(Card)) or 0
        return {"seeded": False, "deck_count": deck_count, "card_count": card_count}

    card_total = 0
    for deck_data in DEVOPS_DECKS:
        deck_payload = dict(deck_data)
        cards = deck_payload.pop("cards")
        deck = Deck(**deck_payload)
        db.add(deck)
        db.flush()
        for card_data in cards:
            db.add(Card(deck_id=deck.id, **card_data))
        card_total += len(cards)

    db.commit()
    return {"seeded": True, "deck_count": len(DEVOPS_DECKS), "card_count": card_total}
