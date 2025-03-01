import os
import uvicorn
from app.main import app

if __name__ == "__main__":
    # Use PORT environment variable if provided (for cloud deployment)
    port = int(os.environ.get("PORT", 8000))
    
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=port, 
        reload=os.environ.get("ENVIRONMENT") != "production"
    )
