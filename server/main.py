from fastapi import FastAPI
from apis import fatsia_routes

app = FastAPI()

# Server entry point
if __name__ == "__main__":
    import uvicorn
    app.include_router(fatsia_routes.router)
    uvicorn.run(app, host="127.0.0.1", port=8000)
