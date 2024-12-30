from app import create_app
import uvicorn

app = create_app()

if __name__ == "__main__":
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
