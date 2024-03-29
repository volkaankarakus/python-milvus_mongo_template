
# Project Setup Instructions

A virtual environment is used to manage project-specific dependencies.
This prevents the libraries your project uses from conflicting with the system-wide Python installation.
You can create the virtual environment as follows:
```
python3 -m venv venv
```

To activate this environment:
```bash
source venv/bin/activate
```

You can install the libraries required for your project using pip. For example, to install the requests library:
```bash
pip3 install requests
```

It is a good practice to list the libraries you have installed in a requirements.txt file.
This file shows what dependencies others need to install when they clone your project.
You can save dependencies in this file like this:
```bash
pip3 freeze > requirements.txt
```

To run this project, you can use the following command in your terminal:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Run in Browser

When your application launches successfully, open your browser and go to `http://localhost:8000/docs`.
FastAPI automatically generates Swagger documentation and you can view and test all routes of your API using this address.

## Upload to GCP

Create a "requirements.txt" file containing the relevant dependencies.
- main.py
- requirements.txt
- app/


## Deploy to Google Cloud Functions

To deploy to Google Cloud Functions, use the following command:
```
gcloud functions deploy (google_cloud_function_name)   --runtime python310   --trigger-http   --allow-unauthenticated   --entry-point main   --project (your-project-id)   --region us-central1
```
