from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


def success_response(data=None, message="Success", status_code=200):
    if isinstance(data, BaseModel):
        data = data.model_dump()

    data = jsonable_encoder(data)
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "success",
            "data": data,
            "message": message,
        },
    )


def error_response(message, status_code=500):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "message": message,
        },
    )
