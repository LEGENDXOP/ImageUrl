from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, os, utils



app = FastAPI(
    title="AnySell API",
    description="API for AnySell",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/uploadImage")
async def upload_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open(file.filename, "wb") as f:
            f.write(contents)

        with open(file.filename, "rb") as image_file:
            image_url = utils.get_image_url(file.filename)
            os.remove(file.filename)
            return {"image_url": image_url}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}
    finally:
        if os.path.exists(file.filename):
            os.remove(file.filename)



if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8080))
    uvicorn.run(
        "main:app",
        host = "0.0.0.0",
        port = PORT,
        reload = True,
        workers = 1
    )