from fastapi import FastAPI
from database import client
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.on_event("startup")
async def startup_db_client():
    try:
        client.admin.command("ping")
        print(
            "Pinged your deployment. You successfully connected to MongoDB! Choose a db"
        )
    except Exception as e:
        print(e)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()