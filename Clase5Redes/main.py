from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/files")
async def return_files(name: str = None):
    if name:
        path = os.path.join("./files", name + ".txt")
        return {"status": "OK", "path": path}
    files = []
    for file in os.listdir("./files"):
        files.append(file)
    return files

@app.post("/create_file")
async def create_file(name: str, content:str):
    try:
        os.makedirs("./files", exist_ok=True)
        path = os.path.join("./files", name + ".txt")
        with open(path, 'w', encoding='utf-8') as archivo:
            archivo.write(content)
        return {"status": "OK", "path": path}
    except Exception as e:
        return {"status": "Error", "detail": str(e)}