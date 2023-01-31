from fastapi import APIRouter, HTTPException
from .. services.gdrive_service import GdriveService
from .. models.models import GsheetRequest

router = APIRouter(prefix="/gdrive-api/vi")

gdrive = GdriveService()

@router.post("/consume", status_code=200)
def consume(params: GsheetRequest):
    return gdrive.get_gsheet(params)