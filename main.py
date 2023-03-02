from fastapi import FastAPI, Request
from config.Config import Config
from embeddings.EmbeddingGenerator import EmbeddingGenerator
from models.Job import Job
from data.JobStore import JobStore
from models.User import User

app = FastAPI()
config = Config()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/jobs/user/{id}")
async def get_jobs_for_user(id: str, request: Request) -> list[Job]:
    embedding_generator = EmbeddingGenerator(config.get("open_ai_models", "embeddings_model"),
                                             config.get("open_ai_models", "completion_model"))
    job_store = JobStore(config.get("vector_store", "environment"), config.get("vector_store", "index_name"))



@app.get("/jobs/embedding/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/jobs/{id}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/jobs")
async def get_jobs():
    print("get_jobs")
    return {
        "jobs": [
            {
                "id": 1,
                "name": "job1",
                "description": "description1",
                "status": "status1",
                "created_at": "2021-01-01",
                "updated_at": "2021-01-01",
            },
            {
                "id": 2,
                "name": "job3",
                "description": "description1",
                "status": "status1",
                "created_at": "2021-01-01",
                "updated_at": "2021-01-01",
            }
        ]
    }