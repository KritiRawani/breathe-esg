# Breathe ESG Tech Intern Assignment

This project is a full-stack ESG data ingestion and analyst review platform built using Django REST Framework and React.

The platform ingests enterprise sustainability data from:
- SAP exports
- Utility electricity data
- Corporate travel data

The system normalizes raw records, calculates emissions, detects suspicious data, and enables analyst approval workflows before audit locking.

# Architecture

Frontend:
- React + Tailwind CSS

Backend:
- Django REST Framework

Database:
- PostgreSQL

Workflow:
Raw Upload → RawRecord → Normalization → EmissionRecord → Analyst Review → Audit Lock

# Features

- Multi-tenant architecture
- SAP CSV ingestion
- Utility data ingestion
- Travel data ingestion
- Raw source tracking
- Emission normalization
- Suspicious record detection
- Analyst review workflow
- Audit logging
- Dashboard analytics

# Tech Stack

Frontend:
- React
- Axios
- Tailwind CSS

Backend:
- Django
- Django REST Framework

Database:
- PostgreSQL

Deployment:
- Render
- Vercel

# Setup Instructions

Backend:
cd backend
python -m venv env
env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Frontend:
cd frontend

npm install

npm run dev

# API Endpoints

POST /api/upload/sap/
POST /api/emissions/normalize/
GET /api/emissions/records/
POST /api/reviews/approve/<id>/
POST /api/reviews/reject/<id>/
POST /api/reviews/lock/<id>/
GET /api/dashboard/summary/

# Deployment Links

Frontend:
[https://your-vercel-url.vercel.app](https://breathe-esg-vert.vercel.app/)

Backend:
[https://your-render-url.onrender.com](https://breathe-esg-enne.onrender.com)

# Tradeoffs

- OCR PDF parsing was not implemented
- Real SAP integrations were simplified
- Async queues were skipped for prototype scope

# Future Improvements

- Async ingestion queues
- OCR utility bill parsing
- Real emission factor APIs
- Authentication and RBAC
- Advanced dashboard analytics
