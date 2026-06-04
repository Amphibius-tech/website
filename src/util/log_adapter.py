import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if os.getenv("VERCEL"):
    handler = logging.StreamHandler()
else:
    os.makedirs("logs", exist_ok=True)
    handler = logging.FileHandler("logs/linkedin.log")

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)