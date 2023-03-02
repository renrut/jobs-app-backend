# Jobs App Backend

### Description
This is still very much a work in progress and not working in it's current state.

The idea behind this app is to create a job discovery system that allows users to see what jobs are out there and give them an idea of what they may want to apply for based on a continual tuning engine.

Using a feedback system based on popular dating apps, users can swipe left or right on jobs they are interested in. The more a user swipes left on a job, the less likely they are to see that sort of listing again. The more a user swipes right on a job, the more likely they are to see more.

### Technologies
This app is built using python and the FastAPI framework. The vector store is hosted on Pinecone free tier, but will be interchangeable with options like Milvus, Redis, or whatever ends up making sense cost vs. performance.
The plan right now is that the tuning engine is built using (OpenAI's) Completion and Embeddings APIs. 

The idea is to use the embeddings api to create a vector representation for all ingested jobs based off of their titles and descriptions and store that in a vector DB. When a user requests to load relevent jobs, the backend will use the Completion model to tune the ideal job description for that user based on some mix of structured and unstructured inputs and generate the embedding for that description to find the generated job description's k nearest neighbors in the vector store to present to the user.

As the user swipes left or right on jobs, the backing data for the generated job description will be updated to reflect the users preferences.

### Setup
#### WIP - this will not work at the moment. Please check the main branch for a working version.

Create a .env file in the root directory with the following variables:
```
OPEN_AI_KEY=your_open_ai_key
PINECONE_KEY=your_pinecone_key
```

Then run the following commands:
```
pip install -r requirements.txt
uvicorn main:app --host <your local ip> --port 8000 --reload
```
