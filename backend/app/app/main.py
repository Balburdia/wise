from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="An wise open-source office seat planning solution.",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    servers=[{"url": "/"}]
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/", include_in_schema=False, response_class=HTMLResponse)
def home():
    """Respond to the browser home url."""
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{app.title}</title>
    </head>
    <body>
        <h2>{app.title}</h2>
        <h3>{app.description}</h3>
        <p>Welcome to our API! The documentation is available in two formats:</p>
        <ul>
            <li><a href="{app.docs_url}">Swagger</a></li>
            <li><a href="{app.redoc_url}">Redoc</a></li>
        </ul>
        <p>Download OpenAPI specification: <a href="{app.openapi_url}">openapi.json</a></p>
    </body>
    </html>"""

app.include_router(api_router, prefix=settings.API_V1_STR)
