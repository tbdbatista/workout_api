from pydantic import UUID4, BaseModel

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True     