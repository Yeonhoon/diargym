from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

# query params: path에 필요한 쿼리들을 받아야 함수 실행.
@app.get('/blog')
def index(limit, pubs: bool=True, sort: Optional[str]=None):
  if pubs == True:
    return {'data':f'{limit} {pubs} blogs from DB'}
  else:
    return {'data':f'{limit} blogs from DB'}

@app.get('/blog/unpublished')
def unpub():
  return {'data':'unpublished'}

# path parameter
@app.get('/blog/{blog_id}')
def blogs(blog_id: int):
  return {'data':blog_id}


@app.get('/blog/{blog_id}/comment')
def about(blog_id: int, limit=10):
  return {'data':blog_id,'comment':limit}


class Blog(BaseModel):
  title: str
  content: str
  published: Optional[bool]
  author: str

# post: async, baseModel from pydantic
@app.post('/blog')
def create_blog(request: Blog):
  return {'data': f'The post {request.title} has been posted!'}


# if __name__ == "__main__":
#   uvicorn.run(app, host='127.0.0.1', port='9000')