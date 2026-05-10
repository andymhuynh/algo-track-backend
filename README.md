# AlgoTrack Backend API

Backend API for tracking DSA practice with authentication and protected routes.

## Tech Stack
- FastAPI
- Python
- SQLAlchemy
- JWT (authentication)

## Features
- User registration & login
- JWT-based authentication
- Protected API endpoints
- CRUD operations for problems

## Live API
https://algo-track-backend-s20y.onrender.com/docs

## Example

curl -X POST "https://algo-track-backend-s20y.onrender.com/problems" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Two Sum","difficulty":"Easy","topic":"Array"}'