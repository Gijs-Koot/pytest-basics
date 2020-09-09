from pathlib import Path
from typing import List
from datetime import datetime

import math
from dataclasses import dataclass
import shapely
import requests
import psycopg2.extras


def badsum(x: int, y: int) -> int:
    # returns the sum of x and y
    return x


def calc_square_root(x: float) -> float:
    return math.sqrt(x)


def writefile(integers: List[int], pth: Path):
    """Given a list of integers and a filepath, this writes 
    the numbers on separate lines, so the file will look like this

    12
    23
    5345
    12
    1

    If the file exists, no writing is done and a valueerror is raised
    """
    if pth.exists():
        raise ValueError("File exists!")

    pth.parent.mkdir(exist_ok=True, parents=True)

    with pth.open('w') as f:
        for integer in integers:
            f.write(f"{integer}\n")


def getexternaldata():
    
    response = requests.get("http://www.google.nl")
    
    with open("data.txt") as f:
        f.write(response.text)


@dataclass
class Building:

    bag_id: str
    startdate: datetime
    exterior: shapely.geometry.LinearRing



def get_buildings(conn: psycopg2.extensions.connection) -> List[Building]:

    with conn.cursor() as cursor:
        sql = """
        SELECT bag_building_id, startdate, exterior FROM nl_data.bag_buildings
        """

        cursor.execute(sql)

        building_data = cursor.fetchall()

    buildings = list()

    for bag_id, startdate, exterior in building_data:

        exterior = shapely.wkb.loads(exterior)

        building = Building(
            bag_id,
            exterior,
            startdate
        )

        buildings.append(building)


def get_buildings_magic(conn: psycopg2.extensions.connection) -> List[Building]:

    with conn.cursor() as cursor:
        sql = """
        SELECT bag_building_id, startdate, exterior FROM nl_data.bag_buildings
        """

        cursor.execute(sql)

        building_data = cursor.fetchall()

    buildings = list()

    for bag_id, startdate, exterior in building_data:

        exterior = shapely.wkb.loads(exterior)

        building = Building(
            bag_id,
            exterior,
            startdate
        )

        buildings.append(building)