import pathlib
from dotenv import load_dotenv
from os import getenv, environ
import logging
from app.aws.ssm import SSMHandler

logger = logging.getLogger(__name__)

def load_envFile():
    base_dir = pathlib.Path(__file__).parent
    if load_dotenv(base_dir.joinpath('.env')) != True:
        logger.error(
            "Enviroment file couldn't be found or there was an error setting enviroment variables.")
    logger.info("The environment variables setting was successful.")


def validate_env():
    vars = [
        "JWT_SECRET",
        "SERVER_DB",
        "PORT_DB",
        "NAME_DB",
        "USER_DB",
        "PASSWORD_DB",
        "AWS_ACCESS_KEY_ID",
        "AWS_SECRET_ACCESS_KEY",
        "AWS_REGION",
    ]
    for i in vars:
        if getenv(i) == None:
            logger.error("Error getting all enviroment variables.")
    logger.info("Starting successful.")


def get_aws():
    ssm_handler = SSMHandler()
    aws_vars = [
        "JWT_SECRET"
    ]
    try:
        for i in aws_vars:
            value = ssm_handler.get_parameter(i)
            if value != None:
                environ[i] = value
                logger.info("value %s has been loaded.", i)
    except:
        logger.error("Error getting the values from AWS.")
    
    else:
        logger.info("Starting successful.")


load_envFile()
get_aws()
validate_env()
