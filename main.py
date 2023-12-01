from fastapi import FastAPI
from database import client, MARMYTHON_DB
from routers.first_router import first_router

app = FastAPI()

app.include_router(first_router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.on_event("startup")
async def startup_db_client():
    try:
        MARMYTHON_DB.command("ping")
        for collection in MARMYTHON_DB.list_collections():
            print(collection)
        print(
            "Pinged your deployment. You successfully connected to MongoDB! Choose a db"
        )
    except Exception as e:
        print(e)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()