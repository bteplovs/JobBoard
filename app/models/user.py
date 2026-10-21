from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str = Field(index=True, unique=False)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str # Change back to hashed password in the future


class UserPublic(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(SQLModel):
    name: str | None = None
    password: str | None = None
