from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.get("/predict")
def predict():
    # simple demo response
    return {"prediction": "hello-aks"}
