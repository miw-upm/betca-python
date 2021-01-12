from fastapi import FastAPI

from rest.auth_resource import auth
from rest.basic_resource import basic
from rest.validation_resource import validation

app = FastAPI(title='BETCA-Python')
app.include_router(basic)
app.include_router(validation)
app.include_router(auth)
