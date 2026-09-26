from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)


from sqlalchemy.orm import Session
from app.services.document import extract_pdf, split_document, create_embedding, create_embeddingTwo
from app.models.document import Document


from app.database.dependency import get_db


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)



@router.post("/upload")
async def upload_document(

    file: UploadFile = File(...),

    db:Session=Depends(get_db)

):


    text = extract_pdf(
        file.file
    )


    chunks = split_document(
        text
    )


    for chunk in chunks:


        # vector = create_embedding(
        #     chunk
        # )

        vector = create_embeddingTwo(
            chunk
        )


        document = Document(

            user_id=1,

            filename=file.filename,

            content=chunk,

            embedding=vector

        )


        db.add(document)



    db.commit()



    return {

        "message":"Document processed",

        "chunks":len(chunks)

    }