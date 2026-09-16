from typing import Optional, List
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    """
       Used in '''post''' and '''put''' requests by client side 
    
    """

    username: str
    email: EmailStr
    password: str

class UserPublicSchema(BaseModel): 
    """
        Used as server response after '''get''' and '''post''' requests for only one user
    """

    id: int
    username: str
    email: EmailStr

class UserUpdateSchema(BaseModel):  # 
    """
        Used in '''put''' requests by client side
    """

    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserListPublicSchema(BaseModel):
    """
        Used as server response after '''get''' requests for more than one user
    """

    users: List[UserPublicSchema]