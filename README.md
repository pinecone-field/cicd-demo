# cicd-demo
This demo attempts to replicate a "mono" repo approach to ci/cd for applications that leverage pinecone. 

## Quickstart
You will need to create a Pinecone account from [Pinecone](https://app.pinecone.io/?sessionType=login) and have an API key that can create three serverless indexes.

### Step #1 - Setup
Add the following to a ```.env``` file.

```PINECONE_API_KEY=[YOUR_API_KEY]```

Create a python virtual environment and install packages required for demo.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run ```python setup.py create``` to create the following indexes:
1. search_ci
1. recommendation_ci
1. genai_ci

These indexes are NOT ephemeral. Pinecone namespaces will allow us to re-use a single index for multiple, simultanenous 
commits.


