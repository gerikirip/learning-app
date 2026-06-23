from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


Difficulty = Literal["new", "again", "good", "easy"]
CardType = Literal["concept", "command", "scenario", "interview", "lab"]
ReviewRating = Literal["again", "good", "easy"]


class CardBase(BaseModel):
    front: str = Field(min_length=1)
    back: str = Field(min_length=1)
    card_type: CardType = "concept"
    difficulty: Difficulty = "new"


class CardCreate(CardBase):
    pass


class CardUpdate(BaseModel):
    front: str | None = Field(default=None, min_length=1)
    back: str | None = Field(default=None, min_length=1)
    card_type: CardType | None = None
    difficulty: Difficulty | None = None


class CardRead(CardBase):
    id: int
    deck_id: int
    last_reviewed_at: datetime | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DeckBase(BaseModel):
    title: str = Field(min_length=1, max_length=160)
    description: str = ""
    topic: str = "general"
    level: str = "beginner"


class DeckCreate(DeckBase):
    pass


class DeckUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=160)
    description: str | None = None
    topic: str | None = None
    level: str | None = None


class DeckRead(DeckBase):
    id: int
    created_at: datetime
    updated_at: datetime
    card_count: int = 0

    model_config = ConfigDict(from_attributes=True)


class DeckDetail(DeckRead):
    cards: list[CardRead]


class ReviewCreate(BaseModel):
    rating: ReviewRating


class ReviewRead(BaseModel):
    id: int
    card_id: int
    rating: ReviewRating
    reviewed_at: datetime

    model_config = ConfigDict(from_attributes=True)
