from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import func_api
import uvicorn


app=FastAPI()


@app.get("/grope")
def get_grope():
    mass_grope= func_api.gettr_all_grope()
    print(mass_grope)
    return {"grope":mass_grope}

@app.get("/raspis/{grope}")
def get_raspis(grope:str):
    j= func_api.json_rasp(grope)
    return j


@app.get("/redact/{grope}")
def get_raspis(grope:str):
    j= func_api.redact(grope, True)
    return j


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__=="__main__":
    uvicorn.run("main:app", reload=True)