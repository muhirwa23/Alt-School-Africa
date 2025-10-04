#!/usr/bin/env python3
"""
Simple script to run the EduTrack Lite API server
"""

import uvicorn

if __name__ == "__main__":
    print("Starting EduTrack Lite API server...")
    print("API Documentation will be available at: http://localhost:8000/docs")
    print("ReDoc Documentation will be available at: http://localhost:8000/redoc")
    print("Press Ctrl+C to stop the server")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload for development
        log_level="info"
    )
