from pydantic import BaseModel,ValidationError


class Tag(BaseModel):
    id : int
    name : str

class City(BaseModel):
    city_id:int
    name: str
    tags: list[Tag]


input_json = """
{
    "city_id": "33231",
    "name": "Moscow",
    "tags": [
    {
    "id": "554", "name": "Nazar"
    },
    {
    "id": "5524", "name": "Nazarov"
    }
    ]
}
"""

try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print(e.json())
else:
    print(city.tags[0].id)
