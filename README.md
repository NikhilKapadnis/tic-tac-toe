# Tic Tac Toe (FastAPI + Docker + AWS ECS)

A simple Tic Tac Toe (X-O) web game built with **FastAPI** backend and a **static HTML/CSS/JS** frontend.  
Designed to be containerized with **Docker** and deployed to **AWS (ECR + ECS Fargate)**.

## Features
- Play Tic Tac Toe in the browser
- You are **X**, computer is **O**
- Backend API for moves
- Health endpoint for load balancers: `/health`
- Ready for Docker + AWS deployment

## Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, JavaScript (served from `/static`)
- **Server:** Uvicorn
- **Container:** Docker (planned)
- **Cloud:** AWS ECR + ECS Fargate (planned)

## Project Structure
├── main.py
├── static
│ ├── index.html
│ ├── styles.css
│ └── app.js
└── .gitignore
