from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5500",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AddCars(BaseModel):
    nomi: str
    modeli: int
    narxi: int | float
    rasmi: str

cars = [
    {
        "id": 1,
        "nomi": "Toyota Supra",
        "modeli": 1984,
        "narxi": 45000,
        "rasmi": "https://images.pexels.com/photos/28569837/pexels-photo-28569837/free-photo-of-dynamic-toyota-supra-mk4-in-motion-on-open-road.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
    },
    {
        "id": 2,
        "nomi": "Nissan Skyline r-34",
        "modeli": 1987,
        "narxi": 50000,
        "rasmi": "https://images.pexels.com/photos/35575126/pexels-photo-35575126.png?cs=srgb&dl=pexels-froydd97-35575126.jpg&fm=jpg"
    },
    {
        "id": 3,
        "nomi": "Chevrolet Malibu",
        "modeli": 2010,
        "narxi": 25000,
        "rasmi": "https://i.pinimg.com/originals/4a/e6/3a/4ae63a3e8123a20ce37071b1aa6daee5.jpg"
    },
    {
        "id": 4,
        "nomi": "BMW M4",
        "modeli": 2015,
        "narxi": 30000,
        "rasmi": "https://images.unsplash.com/photo-1617531653332-bd46c24f2068?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Ym13JTIwbTR8ZW58MHx8MHx8fDA%3D"
    },
    {
        "id": 5,
        "nomi": "Audi R8",
        "modeli": 2018,
        "narxi": 50000,
        "rasmi": "https://images.pexels.com/photos/29157204/pexels-photo-29157204.jpeg?cs=srgb&dl=pexels-sam-mccool-1923523643-29157204.jpg&fm=jpg"
    },
    {
        "id": 6,
        "nomi": "Mercedes-Benz S-Class",
        "modeli": 2020,
        "narxi": 70000,
        "rasmi": "https://images.unsplash.com/photo-1610099610040-ab19f3a5ec35?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWVyY2VkZXMlMjBzJTIwY2xhc3N8ZW58MHx8MHx8fDA%3D"
    },
    {
        "id": 7,
        "nomi": "Lamborghini Huracan",
        "modeli": 2019,
        "narxi": 200000,
        "rasmi": "https://images.unsplash.com/photo-1544636331-e26879cd4d9b?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 8,
        "nomi": "Ferrari 488",
        "modeli": 2016,
        "narxi": 250000,
        "rasmi": "https://images.unsplash.com/photo-1583121274602-3e2820c69888?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 9,
        "nomi": "Porsche 911",
        "modeli": 2021,
        "narxi": 120000,
        "rasmi": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 10,
        "nomi": "Ford Mustang",
        "modeli": 2017,
        "narxi": 35000,
        "rasmi": "https://images.unsplash.com/photo-1494976388531-d1058494cdd8?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 11,
        "nomi": "Dodge Challenger",
        "modeli": 2018,
        "narxi": 40000,
        "rasmi": "https://images.unsplash.com/photo-1612825173281-9a193378527e?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 12,
        "nomi": "Tesla Model S",
        "modeli": 2022,
        "narxi": 90000,
        "rasmi": "https://images.unsplash.com/photo-1560958089-b8a1929cea89?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 13,
        "nomi": "Bugatti Chiron",
        "modeli": 2020,
        "narxi": 3000000,
        "rasmi": "https://images.unsplash.com/photo-1617814076367-b759c7d7e738?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 14,
        "nomi": "Rolls-Royce Ghost",
        "modeli": 2021,
        "narxi": 350000,
        "rasmi": "https://images.unsplash.com/photo-1563720223185-11003d516935?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 15,
        "nomi": "McLaren 720S",
        "modeli": 2019,
        "narxi": 300000,
        "rasmi": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 16,
        "nomi": "Bentley Continental GT",
        "modeli": 2020,
        "narxi": 220000,
        "rasmi": "https://images.unsplash.com/photo-1580274455191-1c62238fa333?fm=jpg&q=60&w=3000&auto=format&fit=crop"
    },
    {
        "id": 17,
        "nomi": "Nissan GT-R R-25",
        "modeli": 2018,
        "narxi": 80000,
        "rasmi": "https://cdn.wallpapersafari.com/81/42/2fIAvh.jpg"
    },
    {
        "id": 18,
        "nomi": "Gelik",
        "modeli": 2021,
        "narxi": 180000,
        "rasmi": "https://images.unsplash.com/photo-1648413653877-ade5eefd2f1b?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZyUyMHdhZ29ufGVufDB8fDB8fHww"
    },
    {
        "id": 19,
        "nomi": "Toyota Supra Mk5",
        "modeli": 2019,
        "narxi": 65000,
        "rasmi": "https://wallpapers.com/images/hd/4k-laptop-car-toyota-supra-3vpo6s8g2wq8xitp.jpg"
    },
    {
        "id": 20,
        "nomi": "Chevrolet Camaro",
        "modeli": 2022,
        "narxi": 70000,
        "rasmi": "https://images2.alphacoders.com/901/901982.jpg"
    },
]


@app.get("/api")
def takeUser():
    return cars


@app.post("/api/add")
def addCars(carsAdd: AddCars):
    new_id = max(car["id"] for car in cars) + 1     
    new_car = carsAdd.dict()
    new_car["id"] = new_id
    cars.append(new_car)
    return f"{new_car['nomi']} qo'shildi"


@app.delete("/api/delete/{car_id}")  
def deleteCars(car_id: int):         
    global cars
    cars = [car for car in cars if car["id"] != car_id]  
    return {"message": f"Car with id {car_id} id li mashina o'chirildi."}
@app.put("/api/update/{car_id}")
def update(car_id: int, updateUser: AddCars):
    for u in cars:
        if u["id"] == car_id:
            u["nomi"] = updateUser.nomi
            u["modeli"] = updateUser.modeli
            u["narxi"] = updateUser.narxi
            u["rasmi"] = updateUser.rasmi
            return f"{updateUser.nomi} yangilandi"
    return {"error": f"{car_id} id li mashina topilmadi"}