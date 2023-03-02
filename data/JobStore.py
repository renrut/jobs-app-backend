import pinecone
from dotenv import load_dotenv, find_dotenv
import os
#
# pinecone.init(api_key="YOUR_API_KEY",
#               environment="us-east1-gcp")

load_dotenv(find_dotenv())

class JobStore:


    def __init__(self, environment, index_name, namespace):
        pinecone.init(api_key=os.environ.get("PINECONE_KEY"), environment=environment)
        self.index = pinecone.Index(index_name)
        self.namespace = namespace
        self.jobs = []

    def get_k_nearest_jobs(self, embedding, k):
        query_response = self.index.query(
            namespace=self.namespace,
            top_k=k,
            include_values=True,
            include_metadata=True,
            vector=embedding
        )
        return query_response