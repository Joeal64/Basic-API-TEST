# Simple Flask API

This is a simple Flask API project.

## Setup

1. Create a virtual environment:
   ```sh
   python -m venv venv
2. Activate virual environnment on Windows
   venv\Scripts\activate
3. Install dependencies 
    pip install -r req.txt

4. Run application
    python app.py

Endpoints
GET /api: Returns a greeting message.
POST /api: Receives JSON data and returns it.
Example Requests
GET:

curl http://127.0.0.1:5000/api

curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://127.0.0.1:5000/api