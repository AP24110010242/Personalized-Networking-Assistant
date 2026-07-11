#!/bin/bash

# Start FastAPI in the background
echo "Starting FastAPI backend..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit in the foreground, using Render's $PORT (or 8501 if local)
echo "Starting Streamlit frontend..."
streamlit run frontend/streamlit_app.py --server.port ${PORT:-8501} --server.address 0.0.0.0
