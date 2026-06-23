from datetime import UTC, datetime

from fastapi import HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.models import Card, Deck, Review
from app.schemas import CardCreate, CardUpdate, DeckCreate, DeckUpdate, ReviewCreate


def deck_to_read(deck: Deck, card_count: int | None = None) -> dict:
    return {
        "id": deck.id,
        "title": deck.title,
        "description": deck.description,
        "topic": deck.topic,
        "level": deck.level,
        "created_at": deck.created_at,
        "updated_at": deck.updated_at,
        "card_count": len(deck.cards) if card_count is None and hasattr(deck, "cards") else card_count or 0,
    }


def list_decks(db: Session) -> list[dict]:
    statement = (
        select(Deck, func.count(Card.id).label("card_count"))
        .outerjoin(Card)
        .group_by(Deck.id)
        .order_by(Deck.topic, Deck.title)
    )
    return [deck_to_read(deck, card_count) for deck, card_count in db.execute(statement).all()]


def get_deck(db: Session, deck_id: int) -> Deck:
    deck = db.scalar(
        select(Deck)
        .options(selectinload(Deck.cards))
        .where(Deck.id == deck_id)
    )
    if deck is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deck not found")
    return deck


def create_deck(db: Session, payload: DeckCreate) -> Deck:
    deck = Deck(**payload.model_dump())
    db.add(deck)
    db.commit()
    db.refresh(deck)
    return deck


def update_deck(db: Session, deck_id: int, payload: DeckUpdate) -> Deck:
    deck = get_deck(db, deck_id)
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(deck, key, value)
    db.commit()
    db.refresh(deck)
    return deck


def delete_deck(db: Session, deck_id: int) -> None:
    deck = get_deck(db, deck_id)
    db.delete(deck)
    db.commit()


def list_cards(db: Session, deck_id: int) -> list[Card]:
    get_deck(db, deck_id)
    return list(db.scalars(select(Card).where(Card.deck_id == deck_id).order_by(Card.id)).all())


def get_card(db: Session, card_id: int) -> Card:
    card = db.get(Card, card_id)
    if card is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Card not found")
    return card


def create_card(db: Session, deck_id: int, payload: CardCreate) -> Card:
    get_deck(db, deck_id)
    card = Card(deck_id=deck_id, **payload.model_dump())
    db.add(card)
    db.commit()
    db.refresh(card)
    return card


def update_card(db: Session, card_id: int, payload: CardUpdate) -> Card:
    card = get_card(db, card_id)
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(card, key, value)
    db.commit()
    db.refresh(card)
    return card


def delete_card(db: Session, card_id: int) -> None:
    card = get_card(db, card_id)
    db.delete(card)
    db.commit()


def review_card(db: Session, card_id: int, payload: ReviewCreate) -> Review:
    card = get_card(db, card_id)
    card.difficulty = payload.rating
    card.last_reviewed_at = datetime.now(UTC)
    review = Review(card_id=card.id, rating=payload.rating)
    db.add(review)
    db.commit()
    db.refresh(review)
    return review
