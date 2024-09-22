from fastapi import FastAPI
from db.postgres import init_db
from routes.transaction import router
import uvicorn


app = FastAPI()

# Initialize the database when the application starts
init_db()

app.include_router(router, prefix="/transactionservice")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000