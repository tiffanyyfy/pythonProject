from fastapi import FastAPI

app = FastAPI()

@app.get("/api/home")
def home ():
    return render_template()

