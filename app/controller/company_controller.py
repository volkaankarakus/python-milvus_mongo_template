from app.service.database import get_mongo_client, get_mongo_database, get_mongo_collection
from app.model.company_model import Company
from bson import ObjectId
from typing import List
from pymongo.errors import DuplicateKeyError
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# MongoDB bağlantı dizesini .env dosyasından oku
MONGODB_EXAMPLE_COLLECTION_NAME = os.getenv('MONGODB_EXAMPLE_COLLECTION_NAME')
MONGODB_EXAMPLE_DB_NAME = os.getenv('MONGODB_EXAMPLE_DB_NAME')

class CompanyAlreadyExistsError(Exception):
    pass

class CompanyController:
    #Constructor
    def __init__(self):
        self.client = get_mongo_client()
        self.database = get_mongo_database(self.client,MONGODB_EXAMPLE_DB_NAME)
        self.collection = get_mongo_collection(self.database,MONGODB_EXAMPLE_COLLECTION_NAME)

    # Get Company by ID
    async def get_company_by_id(self, company_id: str) -> Company:
        result = self.collection.find_one({"_id": ObjectId(company_id)})
        if result:
            return Company(**result)
        else:
            return None

    # Create Company
    async def create_company(self, company_data: Company) -> Company:
        try:
            result = self.collection.insert_one(company_data.dict(by_alias=True, exclude={"id"}))
            company_data.id = str(result.inserted_id)
            return company_data
        except DuplicateKeyError:
            raise CompanyAlreadyExistsError("Company with this code already exists")
        
    # Update Company
    async def update_company(self, company_id: str, company_data: Company) -> Company:
        try:
            query = {"_id": ObjectId(company_id)}
            update_data = {"$set": company_data.dict(exclude_unset=True)}
            result = self.collection.update_one(query, update_data)
            if result.matched_count:
                # Güncellenen şirketi geri döndür
                return await self.get_company_by_id(company_id)
            else:
                # Şirket bulunamadıysa None döndür
                return None
        except Exception as e:
            # Hata durumunda işlemek için bir hata yakalama
            raise e
        
    # Delete Company
    async def delete_company(self, company_id: str) -> bool:
        try:
            query = {"_id": ObjectId(company_id)}
            result = self.collection.delete_one(query)
            return result.deleted_count > 0  # True if a company was deleted, False if not
        except Exception as e:
            # Hata durumunda işlemek için bir hata yakalama
            raise e

    # Get Companies (No need to enclose it in a try-except block)
    async def get_all_companies(self) -> List[Company]:
        companies = self.collection.find()
        return [Company(**company) for company in companies]