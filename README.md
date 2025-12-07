# E-commerce Product Management API

Backend API for managing e-commerce products built with Django & Django REST Framework.

## Project Summary
This project implements Product CRUD, Category management, product images, search and basic user authentication. It follows the Capstone requirements and is being developed iteratively. (See project docs used as reference.)

## Tech
- Python, Django, Django REST Framework
- PostgreSQL (recommended), SQLite for local dev
- Optional: Docker, Gunicorn, Nginx, AWS S3 for media

## Quick start (local)
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## API
Base path: `/api/v1/`  
See `products/` app for product endpoints.

## Notes
This repo contains the initial scaffold and core models and endpoints for the Capstone project. Requirements and planning documents are followed as a guide. See the submitted Google Doc link in the course submission for ERD and API spec.

