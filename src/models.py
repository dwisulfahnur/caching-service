import datetime
from sqlmodel import SQLModel, Field

class Payload(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    output: str

    created_at: datetime.datetime = Field(
        default=datetime.datetime.now(datetime.timezone.utc), 
        nullable=False
    )
