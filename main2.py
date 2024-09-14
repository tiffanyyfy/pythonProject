from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers.apis import router as pda_user_api_router

app = FastAPI(title = '管理员接口测试')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pda_user_api_router)