
from dotenv import load_dotenv

load_dotenv(override=True)

from fastapi import FastAPI

from api.routers.journal_router import router as journal_router

#my imports
import logging
import sys

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)
logging.info(" The API is starting up ")

app = FastAPI(title="Journal API", description="A simple journal API for tracking daily work, struggles, and intentions")
app.include_router(journal_router)


