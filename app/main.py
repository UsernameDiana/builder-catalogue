from fastapi import FastAPI
from app.api import api

app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight": False},
    title="Builder Catalogue API",
    redoc_url=None
)

app.include_router(api.router, prefix="/api", tags=["Catalogue"])
