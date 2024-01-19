from pydantic import BaseModel, Field
from typing import Optional,Union
from datetime import datetime
from bson import ObjectId
from typing import List

class Company(BaseModel):
    id: Optional[str] = Field(None, alias='_id')
    company_code: str
    name: str
    created_at: Optional[datetime] = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda oid: str(oid),  # ObjectId'yi string'e çevirmek için
        }

class CompanyResponse(BaseModel):
    status: str
    company: Union[Optional[Company], Optional[List[Company]]]  # Tek Company veya Company listesi
