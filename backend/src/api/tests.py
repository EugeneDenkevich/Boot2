from src.api.create_app import app


@app.get("/api/test")
async def test():
    return 'test passed successfully'