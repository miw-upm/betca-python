from fastapi import APIRouter

from rest.dtos import Dto

basic = APIRouter(
    prefix="/basic",
    tags=["basic"],
)


@basic.get("/search")
def find(name: str) -> [Dto]:
    return [Dto(id='1', name=name, description='desc'), Dto(id='2', name=name, description='desc2', value=2)]


@basic.post("")
def create(dto: Dto) -> Dto:
    return dto


@basic.get("/{ide}")
def read(ide: str):
    return Dto(id=ide, name="dto", description='desc')


@basic.put("/{ide}")
def update(ide: str, dto: Dto) -> Dto:
    dto.id = ide
    return dto


@basic.delete("/{ide}")
def delete(ide: str):
    print('Dto(', ide, ') deleted')
    return None
