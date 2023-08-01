from fastapi import APIRouter


router = APIRouter(
    prefix='/api-test',
)


@router.get("/", name='Test the server',
            include_in_schema=False)
def check_server():
    return "success"
