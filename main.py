from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
data_store = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/nmea")
async def receive_nmea(req: Request):
    incoming = await req.json()
    data_store.update(incoming)
    return {"status": "ok"}

@app.get("/api/data")
def get_nmea_data():
    return data_store

@app.get("/")
def root():
    return {"status": "running"}
