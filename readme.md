# Deploy

## Requires

- docker

## Deploy

1. create .env  
   Create .env and set params by refering .env_sample

2. run

```
docker compose up -d
```

## build image

```
docker build -t uttechcenter/sample_streamlit_for_openai:v1.0.0 .
```

# Dev

## Requires

- python: 3.10
- libs (written in requirements.txt)

## Setup

1. create python3.10 venv and activate

   ```
   conda create --name python310_streamlit_for_openai_api python=3.10
   conda activate python310_streamlit_for_openai_api
   ```

2. install libs

   ```
   pip install -r requirements.txt
   ```

3. create .env  
   Create .env and set params by refering .env_sample

## Build

1. activate venv

   ```
   conda activate python310_streamlit_for_openai_api
   ```

2. run streamlit

   ```
   streamlit run server.py
   ```

3. check access
   ```
   http://localhost:8501/
   ```
