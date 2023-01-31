from typing import Optional
from pydantic import BaseModel

class GsheetRequest(BaseModel):
    file_id: str
    sheet_name: str
    range: str