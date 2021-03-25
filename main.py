from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'krishna'}}

@app.get('/about')
def index():
    return {'data':"about page"}