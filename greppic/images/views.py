from fastapi import APIRouter

router = APIRouter()


@router.get('/api/v1/images')
async def list():
    return 'Image List'
