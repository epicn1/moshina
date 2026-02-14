from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()
origins = [
    "http://localhost:3000",    # React
    "http://localhost:5173",    # Vite/Vue
    "http://127.0.0.1:5500",    # VS Code Live Server
    "*",                        # Hammasiga ruxsat berish uchun (faqat test rejimida)
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
    "nomi": "Toyota Supra",
    "modeli": 1984,
    "narxi": 45000,
    "rasmi": "https://images.pexels.com/photos/28569837/pexels-photo-28569837/free-photo-of-dynamic-toyota-supra-mk4-in-motion-on-open-road.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
    },
    {
    "nomi": "Nissan Skyline",
    "modeli": 1987,         
    "narxi": 50000,
    "rasmi": "https://images.pexels.com/photos/35575126/pexels-photo-35575126.png?cs=srgb&dl=pexels-froydd97-35575126.jpg&fm=jpg"
    },
    {
    "nomi": "Chevrolet Malibu",
    "modeli": 2010,
    "narxi": 25000,
    "rasmi": "https://i.pinimg.com/originals/4a/e6/3a/4ae63a3e8123a20ce37071b1aa6daee5.jpg"
    },
    {
    "nomi": " BMW M4",
    "modeli": 2015,
    "narxi": 30000,
    "rasmi": "https://images.unsplash.com/photo-1617531653332-bd46c24f2068?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Ym13JTIwbTR8ZW58MHx8MHx8fDA%3D"
    },
    {
    "nomi": "Audi r8",
    "modeli": 2018,
    "narxi": 50000,
    "rasmi": "https://images.pexels.com/photos/29157204/pexels-photo-29157204.jpeg?cs=srgb&dl=pexels-sam-mccool-1923523643-29157204.jpg&fm=jpg"
    },
    {
    "nomi": "Mercedes-Benz S-Class",
    "modeli": 2020,
    "narxi": 70000,
    "rasmi": "https://images.unsplash.com/photo-1610099610040-ab19f3a5ec35?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWVyY2VkZXMlMjBzJTIwY2xhc3N8ZW58MHx8MHx8fDA%3D"
    }
]
@app.get("/api")
def takeUser():
    return cars
@app.post("/api/add")
def addCars(carsAdd: AddCars):
    cars.append(carsAdd.dict())
    return f"{cars} qo'shildi"