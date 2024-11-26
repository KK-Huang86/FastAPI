from fastapi import FastAPI
from enum import Enum

app=FastAPI()

@app.get("/")
def index():
  return {"message":"HELLO WORLD"}

@app.get("/blog/all")
def get_all_blogs():
  return {"message":"所有的blog資料"}

@app.get("/blog/{id}")
def get_blog(id:int):
  return {"data":f"你的blog是第{id}號"}

class BlogType(str,Enum):
    fontend="forntend"
    backend="backend"
    sql="sql"

@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"message":f"Blog 的資料型態是 {type}"}