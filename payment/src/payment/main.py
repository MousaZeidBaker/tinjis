import logging
import os

from fastapi import FastAPI

from payment import routers

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
logging.basicConfig(level=LOGLEVEL)


app = FastAPI()

app.include_router(
    router=routers.v1.health.router,
    tags=["Health"],
)

app.include_router(
    router=routers.v1.payments.router,
    tags=["Payments"],
)
