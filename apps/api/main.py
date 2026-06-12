from fastapi import FastAPI

app = FastAPI(
    title="Sovereign LLM Kubernetes Platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Sovereign LLM Kubernetes Platform API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }