from fastapi import FastAPI, Request
import datetime, time
import utils
import schemas
import models
from fastapi.responses import JSONResponse
import sys, os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import desc
from uuid import uuid4

# Get start time of script
# This is used to calculate uptime, which is exposed in the status endpoint.
ServerStartTime = time.time()

# Initialize the database engine
try:
    DatabaseURL = os.environ.get("DB_URL")
    engine = create_engine(DatabaseURL)
    database = Session(engine)
    databaseModel = models.metadata
    databaseModel.bind = engine
    print("Initialized database engine.")
except Exception as err:
    raise
    sys.exit(1)

# Get root path of the API
rootPath = os.environ.get("API_ROOT_PATH")
if rootPath == None:
    rootPath = "/"

app = FastAPI()
start_time = datetime.datetime.now()
instanceID = str(uuid4())

@app.get(rootPath,
         status_code=200,
         name="API - Root",
         description="Return an error message on the root of the API, since nothing should be performed here.",
         tags=["Information"],
         response_model=schemas.APIRootResponse,
         )
async def root():
    print("Root endpoint called.")
    return {
        "success": False,
        "detail": "This is the root of the API. Nothing should be performed here.",
    }


@app.get(
    rootPath + "stats",
    status_code=200,
    name="API - stats",
    description="Return status information about the API",
    tags=["Information"],
    response_model=schemas.APIStatusResponse,
)
async def status():
    uptime_in_seconds = time.time() - ServerStartTime
    clean_uptime = utils.GetNiceTime(uptime_in_seconds)
    return {
        "hostname": os.uname()[1],
        "uptime": clean_uptime,
        "instanceID": instanceID,
    }
