from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict

app = FastAPI(
    title='Suggestify API',
    description='Suggests songs using a machine learning model.',
    version='0.1',
    docs_url='/',
)

app.include_router(predict.router)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='https?://.*',
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
