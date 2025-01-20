#!/bin/bash

# Run the FastAPI application
uvicorn app.main:app --reload --host localhost
