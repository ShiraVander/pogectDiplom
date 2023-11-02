from enum import Enum
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import random

app = FastAPI()

class PodcastCategory(str, Enum):
    news = "News"
    technology = "Technology"
    education = "Education"
    music = "Music"
    other = "Other"

class Podcast(BaseModel):
    id: int
    title: str
    desc: str #описание
    author: str
    images: str
    create_at: datetime #дата создания
    duration: float #длительность
    category: PodcastCategory
    likes: int
        

def get_data(count: int):
    r = requests.get(
        'https://random-data-api.com/api/v2/users?size=' + str(count))
    return r.json()

def get_name():
    r = requests.get(
        'https://random-word-api.herokuapp.com/word?number=2')
    return ' '.join(r.json())

def get_desc():
    r = requests.get(
        'https://random-word-api.herokuapp.com/word?number=10')
    return ' '.join(r.json())

podcasts = []
count = 0
for i in get_data(5):
    data = i
    
    print(f"loading...{count}%")
    podcast = Podcast(id=count, title=get_name(), desc=get_desc(), author=data["username"], images=data["avatar"], 
                      create_at=datetime.now(), duration=float(f"{random.randint(1, 10)}.{random.randint(1, 10000)}"),
                      category=random.choice(list(PodcastCategory)), likes=random.randint(1, 10000))
    podcast.id = count
    podcasts.append(podcast)
    count += 1
print("Finfsh!!!")


@app.get("/api/podcast")
async def root():
    return {"podcasts": podcasts}


@app.get("/api/podcast/rating") #рэйтинг
async def root():
    return {"podcasts": sorted (podcasts, key=lambda x: x.likes, reverse=True)}


@app.get("/api/podcast/duration") #длительность
async def root():
    return {"podcasts": sorted (podcasts, key=lambda x: x.duration, reverse=True)}