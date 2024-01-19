from fastapi import APIRouter, HTTPException, Depends, status
from app.model.company_model import Company
from app.controller.company_controller import CompanyController, CompanyAlreadyExistsError
from typing import List
from bson import ObjectId
from bson.errors import InvalidId

router = APIRouter()


# Get Company by ID (id is parameter of endpoint)
@router.get("/{company_id}", response_model=Company, status_code=status.HTTP_200_OK)
async def get_company(
    company_id: str,
    controller: CompanyController = Depends(CompanyController)):
    try:
        ObjectId(company_id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid company ID format")
    company = await controller.get_company_by_id(company_id)
    if company is not None:
        return {"status": "success", "company": company}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    

# Create Company with request body    
@router.post("/", response_model=Company, status_code=status.HTTP_201_CREATED)
async def create_company(
    company: Company,
    controller: CompanyController = Depends(CompanyController)):
    try:
        created_company = await controller.create_company(company)
        return {"status": "success", "created_company": created_company}
    except CompanyAlreadyExistsError as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))
    

# Update Company (if it returns detailed data status is 200 OK)
@router.put("/{company_id}", response_model=Company,status_code=status.HTTP_200_OK)
async def update_company(
    company_id: str,
    company_data: Company,
    controller: CompanyController = Depends(CompanyController)
):
    try:
        updated_company = await controller.update_company(company_id, company_data)
        if updated_company:
            return {"status": "success", "updated_company": updated_company}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    

# Delete Company by ID (id is parameter of endpoint)
@router.delete("/{company_id}", response_model=bool, status_code=status.HTTP_204_NO_CONTENT)
async def delete_company(
    company_id: str,
    controller: CompanyController = Depends(CompanyController)
):
    try:
        deleted_company = await controller.delete_company(company_id)
        if not deleted_company:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
        return {"status": "success", "deleted_company": deleted_company}
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid company ID format")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

# Get All Companies (No need to enclose it in a try-except block)
@router.get("/", response_model=List[Company])
async def get_all_companies(controller: CompanyController = Depends(CompanyController)):
    all_companies =  await controller.get_all_companies()
    return {"status": "success", "all_companies": all_companies}
