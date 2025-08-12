from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import uvicorn
import pathlib

import model
from db import engine, get_db
import schema


model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/posts')
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(model.Post).all()

    return posts

@app.post('/posts')
def create_post(post_payload: schema.PostModel, db: Session = Depends(get_db)):
    new_post = model.Post(**post_payload.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


if __name__ == '__main__':
    cwd = pathlib.Path(__file__).parent.resolve()
    uvicorn.run(app=app, host="0.0.0.0", port=8080, log_config=f"{cwd}/log.ini")