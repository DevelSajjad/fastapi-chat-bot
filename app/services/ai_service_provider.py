from sqlalchemy.orm import Session
from app.models.ai_provider  import AIProvider

def create_provider(db:Session, data):
    provider = AIProvider(
        **data.model_dump()
    )


    db.add(provider)

    db.commit()

    db.refresh(provider)


    return provider

def get_providers(db:Session):

    return db.query(
        AIProvider
    ).all()


def get_provider(
    db:Session,
    provider_id:int
):

    return db.query(
        AIProvider
    ).filter(
        AIProvider.id==provider_id
    ).first()

def update_provider(
    db:Session,
    provider,
    data
):

    for key,value in data.model_dump(
        exclude_unset=True
    ).items():

        setattr(
            provider,
            key,
            value
        )


    db.commit()

    db.refresh(provider)


    return provider



def delete_provider(
    db:Session,
    provider
):

    db.delete(provider)

    db.commit()