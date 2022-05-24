"""Codecademy School Catalog Project in Dataclass syntax with Enum."""

import typing
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
    pickup_policy: typing.Optional[str] = None

    @property
    def school_info(self) -> str:
        """Returns general School Info"""
        return f"A {self.school_level.value} school named {self.school_name!r} with {self.number_of_students} students."


@dataclass
class MiddleSchool(School):
    """Class representing the Middle School"""

    @property
    def school_info(self) -> str:
        """Adds Pickup Policy information"""
        return f"{super().school_info} The pickup policy is: {self.pickup_policy}"


@dataclass
class PrimarySchool(School):
    """Primary School class"""

    @property
    def school_info(self) -> str:
        """Adds Pickup Policy information"""
        return f"{super().school_info} The pickup policy is: {self.pickup_policy}"


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


class InstancesHolder:
    """Holds the class instances"""

    mySchool = MiddleSchool(
        school_name="Codecademy Middle",
        school_level=SchoolLevels.MIDDLE,
        number_of_students=100,
        pickup_policy="Pickup by parent or guardian",
    )
    myPrimary = PrimarySchool(
        school_name="Codecademy Primary",
        school_level=SchoolLevels.PRIMARY,
        number_of_students=300,
        pickup_policy="Pickup Allowed",
    )
    myHighSchool = HighSchool(
        school_name="Codecademy High",
        school_level=SchoolLevels.HIGH,
        number_of_students=500,
        sports_teams=["Tennis", "Basketball"],
    )


def main():
    """Main program"""

    mySchool = InstancesHolder.mySchool
    myPrimary = InstancesHolder.myPrimary
    myHighSchool = InstancesHolder.myHighSchool

    myHighSchool.addTeam("Hockey")

    schools = [mySchool, myPrimary, myHighSchool]

    for school in schools:
        print(school.school_info)


if __name__ == "__main__":
    main()
