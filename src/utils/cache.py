import json
import hashlib
from typing import Optional
from sqlmodel import Session, select
from src.models import Payload
from src.schemas import PayloadRequest
from src.services.transformer import transform_payload


def generate_identifier(list_1, list_2):
    """
    Generates a unique identifier by concatenating two lists, serializing the result to JSON, 
    and creating an MD5 hash of the serialized string.

    Args:
        list_1 (list): The first list of elements to include in the identifier.
        list_2 (list): The second list of elements to include in the identifier.

    Returns:
        str: The MD5 hash of the concatenated lists, used as a unique identifier.
    """
    concatenated = json.dumps(list_1 + list_2)
    return hashlib.md5(concatenated.encode()).hexdigest()


def get_or_create_payload(session: Session, identifier: str, payload_request: PayloadRequest) -> tuple[Payload, bool]:
    """
    Retrieves an existing payload from the database by its identifier, or creates and stores a new one 
    if it doesn't exist.

    Args:
        session (Session): The database session.
        identifier (str): The unique identifier for the payload.
        payload_request (PayloadRequest): The request schema containing the lists `list_1` and `list_2`.

    Returns:
        tuple[Payload, bool]: A tuple containing the Payload object and a boolean value indicating 
                              whether a new payload was created (True) or retrieved (False).
    """
    payload = session.get(Payload, identifier)
    if payload:
        return payload, False

    transformed_output = transform_payload(
        list_1=payload_request.list_1,
        list_2=payload_request.list_2,
    )

    new_payload = Payload(id=identifier, output=transformed_output)
    session.add(new_payload)
    session.commit()
    return new_payload, True


def get_payload_by_id(session: Session, id: str) -> Optional[Payload]:
    """
    Retrieves a payload from the database by its unique identifier.

    Args:
        session (Session): The database session.
        id (str): The unique identifer of the payload.

    Returns:
        Payload: The payload object if found, otherwise `None`.
    """
    query = select(Payload).where(Payload.id == id)
    payload = session.exec(query).first()
    return payload
