import logging

logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()
