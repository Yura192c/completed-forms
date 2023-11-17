from fastapi import APIRouter, HTTPException, Request
from motor.motor_asyncio import AsyncIOMotorCursor

from config.database import async_collection
from config.form_templates import add_templates
from service.services import get_field_type
from service.field_types import FieldTypes

router = APIRouter()


@router.on_event("startup")
async def on_startup():
    await add_templates()


@router.post("/get_form", description="Получение нужной формы для данных")
async def get_form(request: Request):
    params = request.query_params
    async_cursor: AsyncIOMotorCursor = async_collection.find()
    async for template in async_cursor:
        if all(
                field_name in params.keys()
                and get_field_type(params[field_name]) == template[field_name]
                for field_name in template.keys()
                if field_name not in ('_id', 'name')
        ):
            return {"template_name": template["name"]}

    typed_fields = {field_name: get_field_type(value) for field_name, value in params.items()}
    return typed_fields


@router.post("/add_template", description="Добавление шаблона в бд")
async def add_template(template_data: dict[str, FieldTypes]):
    name: str = "&".join(template_data.keys())
    data = {"name": name, **template_data}

    result = await async_collection.insert_one(data)

    if result.inserted_id:
        return {
            "message": "Template added successfully",
            "template_id": str(result.inserted_id),
            "template_name": str(name)
        }
    else:
        raise HTTPException(status_code=500, detail="Failed to add template to the database")
