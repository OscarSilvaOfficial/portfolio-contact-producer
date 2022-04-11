from fastapi import FastAPI
from app.main.routes import ROUTES
from app.main.configs.cors import CORS

app = FastAPI(title="FastAPI Contact", version='1.0.0')

for route in ROUTES:
  app.include_router(route)

app.add_middleware(**CORS)
