from pydantic import BaseModel, model_validator, Field, ValidationError
from enum import Enum
from datetime import datetime
from typing import Self


class CrewRank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_id(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission_id must start with 'M'")
        return self

    @model_validator(mode="after")
    def check_rank(self) -> Self:
        rank_validator = False
        for member in self.crew:
            if member.rank == CrewRank.COMMANDER or \
               member.rank == CrewRank.CAPTAIN:
                rank_validator = True

        if rank_validator is not True:
            raise ValueError("Mission must have at least one Commander"
                             " or Captain")
        return self

    @model_validator(mode="after")
    def check_exp(self) -> Self:
        experienced = 0
        for member in self.crew:
            if member.years_experience >= 5:
                experienced += 1
        if self.duration_days > 365 and experienced < len(self.crew) / 2:
            raise ValueError("Long missions (> 365 days) need 50% experienced"
                             " crew (5+ years)")
        return self

    @model_validator(mode="after")
    def check_activity(self) -> Self:
        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("========================================")
    print("Valid mission created:")
    try:
        space_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2025, 7, 18),
            duration_days=900,
            mission_status="planned",
            crew=[
                CrewMember(
                    member_id="SC001",
                    name="Sarah Connor",
                    rank=CrewRank.COMMANDER,
                    age=35,
                    specialization="Mission Command",
                    years_experience=7,
                    is_active=True
                ),
                CrewMember(
                    member_id="JS001",
                    name="John Smith",
                    rank=CrewRank.LIEUTENANT,
                    age=34,
                    specialization="Navigation",
                    years_experience=14,
                    is_active=True
                ),
                CrewMember(
                    member_id="AJ001",
                    name="Alice Johnson",
                    rank=CrewRank.OFFICER,
                    age=45,
                    specialization="Engineering",
                    years_experience=21,
                    is_active=True
                )
            ],
            budget_millions=2500.0
        )
        print(f"Mission: {space_mission.mission_name}")
        print(f"ID: {space_mission.mission_id}")
        print(f"Destination: {space_mission.destination}")
        print(f"Duration: {space_mission.duration_days} days")
        print(f"Budget: ${space_mission.budget_millions}M")
        print(f"Crew size: {len(space_mission.crew)}")
        print("Crew members:")
        for member in space_mission.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f"- {member.specialization}")
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    print("\n========================================")
    print("Excepted validation error:")
    try:
        space_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2025, 7, 18),
            duration_days=900,
            mission_status="planned",
            crew=[
                CrewMember(
                    member_id="SC001",
                    name="Sarah Connor",
                    rank=CrewRank.CADET,
                    age=35,
                    specialization="Mission Command",
                    years_experience=7,
                    is_active=True
                ),
                CrewMember(
                    member_id="JS001",
                    name="John Smith",
                    rank=CrewRank.OFFICER,
                    age=45,
                    specialization="Navigation",
                    years_experience=14,
                    is_active=True
                ),
                CrewMember(
                    member_id="AJ001",
                    name="Alice Johnson",
                    rank=CrewRank.LIEUTENANT,
                    age=34,
                    specialization="Engineering",
                    years_experience=21,
                    is_active=True
                )
            ],
            budget_millions=2500.0
        )
        print(f"Mission: {space_mission.mission_name}")
        print(f"ID: {space_mission.mission_id}")
        print(f"Destination: {space_mission.destination}")
        print(f"Duration: {space_mission.duration_days} days")
        print(f"Budget: ${space_mission.budget_millions}M")
        print(f"Crew size: {len(space_mission.crew)}")
        print("Crew members:")
        for member in space_mission.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f"- {member.specialization}")
    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
