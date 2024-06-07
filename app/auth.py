from fastapi import Request, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from jose import JWTError, jwt
import secrets

from starlette.responses import Response


#create the secret key for encoding and decoding JSON Web Tokens (JWTs)
SECRET_KEY = "fast-api"

#algorithm used for signing and verifying JWTs
ALGORITHM = "HS256"

security = HTTPBasic

class AuthMiddleware(BaseHTTPMiddleware) :
    async def dispatch(self, request: Request, call_next) : 
        if request.url.path in ["/login", "/"]:
             return await call_next(request)
        
        credentials :  HTTPBasicCredentials = await security(request)
        username =  credentials.username 
        password = credentials.password 

        if username != "user" or not secrets.compare_digest(password, "password"):
            raise HTTPException(status_code = 401, detail=" Invalid Credentials")
        
        token = jwt.encode({"sub" : username}, SECRET_KEY, algorithm=ALGORITHM)
        request.state.user =  username
        response = await call_next(request)
        response.headers["Authorization"] = f"Bearer, {token}"
        return response