from fastapi import APIRouter

from rest.dtos import Dto, ValidationDto

validation = APIRouter(
    prefix="/validation",
    tags=["validation"],
)


@validation.post("/")
def create(validation_dto: ValidationDto) -> ValidationDto:
    return validation_dto


