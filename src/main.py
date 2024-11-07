import time
from fastapi import FastAPI
from src.handlers import router

app = FastAPI(title='Caching Service')


@app.middleware("http")
async def add_process_time_header(request, call_next):
    """
    this middleware will add a header to the response for every request.
    will be useful to benchmark the request time.
    """
    start_time = time.monotonic()
    response = await call_next(request)
    process_time = time.monotonic() - start_time
    response.headers["X-Process-Time"] = f"{process_time * 1000:.2f} ms"

    return response


app.include_router(router=router)
