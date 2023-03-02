import openai
from prompts.Prompts import JOB_DESCRIPTION_PROMPT
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.environ.get("OPEN_AI_KEY")


class EmbeddingGenerator:
    def __init__(self, embeddings_model, completion_model, description_max_length = 1000):
        self.embeddings_model = embeddings_model
        self.completion_model = completion_model
        self.max_length = description_max_length

    def generate_job_description_for_user(self, user):
        prompt_for_job = JOB_DESCRIPTION_PROMPT + user.interests
        messages = [{"role": "user", "content": prompt_for_job}]

        response = openai.Completion.create(
            model=self.completion_model,
            prompt=messages,
            temperature=0.0
        )
        return response.choices[0].text

    def generate_embeddings_for_user(self, user):
        job_description = self.generate_job_description_for_user(user)
        response = openai.Embedding.create(
            model=self.embeddings_model,
            input=job_description
        )
        return response