from fastapi import FastAPI
from settings import settings  # Import the settings instance

app = FastAPI()

@app.get("/values")
def read_all_variables():
    values = settings.get_all_attributes()
    return values

@app.get("/value/{variable}")
def read_variable(variable: str):
    value = settings.get_attribute(variable)
    return {variable: value}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
