from fastapi import FastAPI

app = FastAPI(title="Leisurely")

@app.get("/health")
async def health_check():
    return {"status": "ok"}