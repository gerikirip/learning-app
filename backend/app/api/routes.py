from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import (
    CardCreate,
    CardRead,
    CardUpdate,
    DeckCreate,
    DeckDetail,
    DeckRead,
    DeckUpdate,
    ReviewCreate,
    ReviewRead,
)
from app.services import learning_service

router = APIRouter(prefix="/api", tags=["learning"])


@router.get("/decks", response_model=list[DeckRead])
def list_decks(db: Session = Depends(get_db)) -> list[dict]:
    return learning_service.list_decks(db)


@router.post("/decks", response_model=DeckRead, status_code=status.HTTP_201_CREATED)
def create_deck(payload: DeckCreate, db: Session = Depends(get_db)):
    deck = learning_service.create_deck(db, payload)
    return learning_service.deck_to_read(deck, 0)


@router.get("/decks/{deck_id}", response_model=DeckDetail)
def get_deck(deck_id: int, db: Session = Depends(get_db)):
    deck = learning_service.get_deck(db, deck_id)
    result = learning_service.deck_to_read(deck)
    result["cards"] = deck.cards
    return result


@router.put("/decks/{deck_id}", response_model=DeckRead)
def update_deck(deck_id: int, payload: DeckUpdate, db: Session = Depends(get_db)):
    deck = learning_service.update_deck(db, deck_id, payload)
    return learning_service.deck_to_read(deck)


@router.delete("/decks/{deck_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deck(deck_id: int, db: Session = Depends(get_db)) -> None:
    learning_service.delete_deck(db, deck_id)


@router.get("/decks/{deck_id}/cards", response_model=list[CardRead])
def list_cards(deck_id: int, db: Session = Depends(get_db)):
    return learning_service.list_cards(db, deck_id)


@router.post("/decks/{deck_id}/cards", response_model=CardRead, status_code=status.HTTP_201_CREATED)
def create_card(deck_id: int, payload: CardCreate, db: Session = Depends(get_db)):
    return learning_service.create_card(db, deck_id, payload)


@router.put("/cards/{card_id}", response_model=CardRead)
def update_card(card_id: int, payload: CardUpdate, db: Session = Depends(get_db)):
    return learning_service.update_card(db, card_id, payload)


@router.delete("/cards/{card_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_card(card_id: int, db: Session = Depends(get_db)) -> None:
    learning_service.delete_card(db, card_id)


@router.post("/cards/{card_id}/reviews", response_model=ReviewRead, status_code=status.HTTP_201_CREATED)
def review_card(card_id: int, payload: ReviewCreate, db: Session = Depends(get_db)):
    return learning_service.review_card(db, card_id, payload)
