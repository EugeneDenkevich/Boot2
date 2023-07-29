from fastapi import APIRouter


router = APIRouter(
    prefix='/api-test',
    
)


@router.get("/", name='Test the server', tags=["Tests"])
def check_server():
    return "success"
