from random import choices
from ninja import Schema

class MassageOut(Schema):
    detail: str



class AuthOut(Schema):
    name : str
    email : str = None
    phone : str = None



class ProductIn(Schema):
    name : str
    price : float
    image : str
    is_active : bool
    is_DrawTool : bool
    is_rare : bool
    # language : int = 'AB'
    # category : str = 'Art'
    auth_id : int = None


class ProductOut(ProductIn):
    id : int
    name : str
    price : float
    image : str = None
    is_active : bool
    is_DrawTool : bool
    is_rare : bool
    auth : AuthOut = None

class AuOut(Schema):
    id : int
    name: str
    email : str = None
    phone :str


class ProOut(Schema):
    id : int
    name : str
    price : float
    auth : AuOut = None


class CartOut(Schema):
    id: int
    customer: str
    product: str
    quantity: int


class CartIn(Schema):
    customer: str
    product: str
    quantity: int


class OrderOut(Schema):
    items: str
    total: float
    price: float
    order_date: int
    C_id: int
    branch: int
    E_id: int
    Delivery_type: int
