import pathlib
from dotenv import load_dotenv
from os import getenv
import logging


logger = logging.getLogger(__name__)

def load_envFile():
    base_dir = pathlib.Path(__file__).parent
    if load_dotenv(base_dir.joinpath('.env')) != True:
        logger.error(
            "Enviroment file couldn't be found or there was an error setting enviroment variables.")
    logger.info("The environment variables setting was successful.")


def validate_env():
    vars = [
        "jwt_hash",
    ]
    for i in vars:
        if getenv(i) == None:
            logger.error("Error getting all enviroment variables.")
    logger.info("Starting successful.")


load_envFile()
validate_env()
