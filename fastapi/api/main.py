from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import router
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

# 🟢 Add CORS middleware here
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # Allow specific origins
    allow_credentials=True,    # Allow Cookies
    allow_methods=["*"],       # Allow all HTTP methods
    allow_headers=["*"],       # Allow all headers
)

# Include your router after CORS
app.include_router(router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my API 🚀"}
