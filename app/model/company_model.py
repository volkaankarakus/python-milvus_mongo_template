from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId  # ObjectId için eklendi

class Company(BaseModel):
    id: Optional[str] = Field(None, alias='_id')
    company_code: str
    name: str
    created_at: Optional[datetime] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str  # ObjectId'yi string'e çevirmek için
        }