from pydantic import BaseModel,EmailStr
class person(BaseModel):
    name:str
    age:int
    email:EmailStr
valid_data=person(name="Dhanush",age=50,email="example@gmail.com")
print(valid_data)