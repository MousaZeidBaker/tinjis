import logging
import random
from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/v1")


class Payment(BaseModel):
    """
    Payment model
    """

    currency: Any
    value: float
    customer_id: str


class PaymentResponse(BaseModel):
    """
    Payment response model
    """

    result: bool


@router.post("/payments", response_model=PaymentResponse)
def create_payment(payment: Payment):
    result = random.choice([True, False])
    if not result:
        logging.info(f"Payment failed for customer id {payment.customer_id}")
    return PaymentResponse(
        result=result,
    )
