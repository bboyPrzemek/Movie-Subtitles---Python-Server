from fastapi import FastAPI
import SubtitlesService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:50291",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/{movieId}")
def get_words(movieId):
    
    unique_words = SubtitlesService.get_unique_words_from_subtitles(movieId)
    #print(unique_words)
    print("Received request for movie ID:", movieId)
    return ["The", "Angel", "home", "is", "where", "the", "heart", "is"]
    #return unique_words
   