from datetime import datetime
from uuid import UUID
class report:
    ID :int
    Subject:str
    Text :str
    CreatedDate: datetime
    creator:UUID
    Receiver:UUID