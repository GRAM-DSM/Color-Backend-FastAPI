from fastapi import FastAPI

import uvicorn

from server.apps import like

app = FastAPI()

app.include_router(like.router)

if __name__ == '__main__':
    uvicorn.run("server.main:app", host="0.0.0.0", reload=True)
