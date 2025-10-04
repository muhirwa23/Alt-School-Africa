from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import users, courses, enrollments

# Create FastAPI app
app = FastAPI(
    title="EduTrack Lite API",
    description="A system for managing course enrollments and tracking course completion",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(enrollments.router)


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to EduTrack Lite API",
        "version": "1.0.0",
        "description": "A system for managing course enrollments and tracking course completion",
        "endpoints": {
            "users": "/users",
            "courses": "/courses", 
            "enrollments": "/enrollments"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
