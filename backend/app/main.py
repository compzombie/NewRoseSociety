import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .api.endpoints import router as api_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

# Get the directory of the frontend build
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend", "build")

# Mount static files if the directory exists
if os.path.isdir(FRONTEND_DIR):
    # Serve static files (JS, CSS)
    app.mount("/static", StaticFiles(directory=os.path.join(FRONTEND_DIR, "static")), name="static")
    
    @app.get("/")
    async def serve_frontend_index():
        index_path = os.path.join(FRONTEND_DIR, "index.html")
        if os.path.exists(index_path):
            return FileResponse(index_path)
        return {"message": "Welcome to the FastAPI application!"}
    
    @app.get("/{catch_all:path}")
    async def serve_frontend_paths(catch_all: str):
        # Check if the path exists as a file in the build directory
        file_path = os.path.join(FRONTEND_DIR, catch_all)
        if os.path.isfile(file_path):
            return FileResponse(file_path)
        
        # Otherwise return the index.html for client-side routing
        index_path = os.path.join(FRONTEND_DIR, "index.html")
        if os.path.exists(index_path):
            return FileResponse(index_path)
        
        # Fallback if file doesn't exist
        raise HTTPException(status_code=404, detail="File not found")
else:
    # Fallback API route if frontend build directory doesn't exist
    @app.get("/")
    def read_root():
        return {"message": "Welcome to the FastAPI application!"}