from fastapi import APIRouter


router = APIRouter(
    prefix='/api-test'
)


@router.get("/")
def check_server():
    return "success"