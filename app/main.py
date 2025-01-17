from app.api import api
from app.database import engine
from app.models import Base
from fastapi import FastAPI

app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight": False},
    title="Builder Catalogue API",
    redoc_url=None,
)

Base.metadata.create_all(bind=engine)

app.include_router(api.router, prefix="/api", tags=["Catalogue"])
