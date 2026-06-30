from typing import Optional, List
from sqlalchemy.orm import Session
from models.category import Category
from schemas.category import CategoryCreate, CategoryResponse
from repositories.category_repository import CategoryRepository
from fastapi import HTTPException, status

class CategoryService:
	def __init__(self, db: Session):
		self.repository = CategoryRepository(db)

	def get_all_categories(self) -> List[CategoryResponse]:
		categories = self.repository.get_all()
		return [CategoryResponse.model_validate(cat) for cat in categories]

	def get_category_by_id(self, category_id: int) -> CategoryResponse:
		category = self.repository.get_by_id(category_id)
		if not category:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"category with id {category_id}")
		return CategoryResponse.model_validate(category)
	
	def create_category(self, category_data: CategoryCreate) -> CategoryResponse:
		return CategoryResponse.model_validate(self.repository.create(category_data))
