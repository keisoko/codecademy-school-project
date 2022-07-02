"""Codecademy School Catalog Project in Dataclass syntax with Enum."""

from dataclasses import dataclass, field
from enum import Enum


class SchoolLevels(Enum):
    """School Levels"""

    MIDDLE = "middle"
    PRIMARY = "primary"
    HIGH = "high"


@dataclass(slots=True)
class School:
    """Parent class representing the School"""

    school_name: str
    school_level: SchoolLevels
    number_of_students: int

    @property
    def school_info(self) -> str:
        """Returns general School Info"""
        return f"A {self.school_level.value} school named {self.school_name!r} with {self.number_of_students} students."


@dataclass
class PrimarySchool(School):
    """Primary School class"""

    pickup_method: str

    @property
    def school_info(self) -> str:
        """Adds Pickup Policy information"""
        return f"{super().school_info} The pickup method is: {self.pickup_method!r}"


@dataclass
class MiddleSchool(School):
    """Class representing the Middle School"""

    pickup_policy: str

    @property
    def school_info(self) -> str:
        """Adds Pickup Policy information"""
        return f"{super().school_info} The pickup policy is: {self.pickup_policy!r}"


@dataclass
class HighSchool(School):
    """High School class"""

    sports_teams: list[str] = field(default_factory=list)

    @property
    def school_info(self) -> str:
        """Adds Information about the sports teams"""
        return f"{super().school_info} It includes the following sports teams: {self.sports_teams}"

    def addTeam(self, team: str) -> None:
        """Appends a new team to the sportsTeams list"""
        self.sports_teams.append(team)


my_primary = PrimarySchool(
    school_name="Codecademy Primary",
    school_level=SchoolLevels.PRIMARY,
    number_of_students=300,
    pickup_method="Students ride on the bus",
)
my_middle_school = MiddleSchool(
    school_name="Codecademy Middle",
    school_level=SchoolLevels.MIDDLE,
    number_of_students=100,
    pickup_policy="Pickup by parent or guardian",
)
my_high_school = HighSchool(
    school_name="Codecademy High",
    school_level=SchoolLevels.HIGH,
    number_of_students=500,
    sports_teams=["Tennis", "Basketball"],
)


def main():
    """Main program"""

    my_high_school.addTeam("Hockey")

    schools = [my_primary, my_middle_school, my_high_school]

    for school in schools:
        print(school.school_info)


if __name__ == "__main__":
    main()
