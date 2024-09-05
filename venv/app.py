from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="mi primer fast api",
    description="soy un webo",
    openapi_tags=[{
        "name":"user",
        "description":"users routes"
    }]
)

app.include_router(user)