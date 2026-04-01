from pydantic import BaseModel, model_validator, Field, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional, Self


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_contact(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        return self

    @model_validator(mode='after')
    def check_physical(self) -> Self:
        if self.contact_type == ContactType.PHYSICAL and \
           self.is_verified is False:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode='after')
    def check_telepathic(self) -> Self:
        if self.contact_type == ContactType.TELEPATHIC and \
           self.witness_count < 3:
            raise ValueError("Telepathic contact requires at "
                             "least 3 witnesses")
        return self

    @model_validator(mode='after')
    def check_signals(self) -> Self:
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2025, 12, 4),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'")
    except ValidationError as e:
        print(e)

    print()
    print("======================================")
    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2025, 11, 3),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=23,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print(f"ID: {invalid_contact.contact_id}")
        print(f"Type: {invalid_contact.contact_type.value}")
        print(f"Location: {invalid_contact.location}")
        print(f"Signal: {invalid_contact.signal_strength}/10")
        print(f"Duration: {invalid_contact.duration_minutes} minutes")
        print(f"Witnesses: {invalid_contact.witness_count}")
        print(f"Message: {invalid_contact.message_received}")
    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
