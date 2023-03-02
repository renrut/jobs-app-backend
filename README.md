# Jobs App Backend

### Description
This is still very much a work in progress and not working in it's current state.

The idea behind this app is to create a simple job board that allows users to see what sort of jobs are out there based on a continual tuning engine.
Using a feedback system based on popular dating apps, users can swipe left or right on jobs they are interested in. The more a user swipes left on a job, the less likely they are to see that sort of listing again. The more a user swipes right on a job, the more likely they are to see more.

### Technologies
This app is built using python and the FastAPI framework. The vector store is hosted on Pinecone free tier, but will be interchangeable with options like Milvus, Redis, or whatever ends up making sense cost vs. performance.
The plan right now is for the tuning engine is built using GPT-3.5-Turbo and OpenAIs embeddings api. The idea is to use the embeddings api to create a vector representation of the job description and then use GPT-3.5-Turbo to tune the ideal job description for a user based on some mix of structured and unstructured inputs and find the generated job descriptions k nearest neighbors to present to the user.
As the user swipes left or right on jobs, the backing data for the generated job description will be updated to reflect the users preferences.

### Setup
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
