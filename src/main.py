from fastapi import FastAPI

from .employees.router import router as employees_router

app = FastAPI(
    title='HB_project',
    summary='A service for birthday greetings.',
    version='0.0.1',
    license_info={
        'name': 'HB_project'
    }
)
app.include_router(employees_router)
