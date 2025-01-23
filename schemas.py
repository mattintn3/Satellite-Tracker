from __future__ import annotations
from typing import Optional, List, Dict
import uuid, json
from uuid import UUID

from pydantic import BaseModel, Field, Json, SecretStr
from datetime import datetime

class User(BaseModel):
    class Config:
        orm_mode = True
        from_attributes = True

    id: str
    username: str = "username"
    email: str
    password: SecretStr
    # totp: bool = False
    # totpSecret: SecretStr = None
    active: bool
    created: datetime
    lastActivity: datetime
    exists: bool = False
    isBanned: bool = False
    isAdmin: bool = False

# API Models

class APIUserCreate(BaseModel):
    username: str
    email: str
    password: str

# API Responses

class APIRootResponse(BaseModel):
    success: bool = False
    detail: str = "This is the root of the API. Please use a valid endpoint."
    
class APIStatusResponse(BaseModel):
    success: bool = True
    name: str = "Satellite Tracker API"
    uptime: str = "0000:00:00:00"
    instanceID: str = "uuid4"
    
    

# API Errors

class GenericError (BaseModel):
    success: bool = False
    detail: str = "An error has occurred."
    
class GenericFatalError (BaseModel):
    success: bool = False
    detail: str = "A fatal error has occurred. Please contact the administrator."

class GenericNotFoundError (BaseModel):
    success: bool = False
    detail: str = "The requested resource was not found."

class GenericUserNotAuthorizedError (BaseModel):
    success: bool = False
    detail: str = "You are not authorized to perform this action."
    