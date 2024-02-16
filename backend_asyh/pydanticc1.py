from pydantic import BaseModel,ValidationError,validator,Field,field_validator


class City(BaseModel):
    city_id: int
    name: str = Field(alias="cityFullName")

    @field_validator("name")
    def name_should_be_sbp(cls, v: str):
        if "spb" not in v.lower():
            raise ValueError("work with SPB!")
        return v
    

input_json = """
{
    "city_id": "33231",
    "cityFullName":"Spb"
}
"""

try:
    city = City.parse_raw(input_json)

except ValidationError as e:
    print("Exeption", e.json())

else:
    print(city.json(by_alias=True))