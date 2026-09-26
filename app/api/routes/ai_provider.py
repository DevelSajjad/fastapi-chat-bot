from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)


from sqlalchemy.orm import Session
from app.database.dependency import get_db
from app.schemas.ai_provider import *
from app.services.ai_service_provider import *



router = APIRouter(
    prefix="/ai-provider",
    tags=["AI Provider"]
)


@router.post("/")
def create(
    data:AIProviderCreate,
    db:Session=Depends(get_db)
):

    return create_provider(
        db,
        data
    )


@router.get("/")
def index(
    db:Session=Depends(get_db)
):

    return get_providers(db)


@router.get("/{id}")
def show(
    id:int,
    db:Session=Depends(get_db)
):

    provider=get_provider(
        db,
        id
    )


    if not provider:

        raise HTTPException(
            404,
            "Provider not found"
        )


    return provider


@router.put("/{id}")
def update(
    id:int,
    data:AIProviderUpdate,
    db:Session=Depends(get_db)
):

    provider=get_provider(
        db,
        id
    )


    if not provider:

        raise HTTPException(
            404,
            "Provider not found"
        )


    return update_provider(
        db,
        provider,
        data
    )



@router.delete("/{id}")
def delete(
    id:int,
    db:Session=Depends(get_db)
):

    provider=get_provider(
        db,
        id
    )


    if not provider:

        raise HTTPException(
            404,
            "Provider not found"
        )


    delete_provider(
        db,
        provider
    )


    return {
        "message":"Deleted successfully"
    }