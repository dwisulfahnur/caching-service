from fastapi import APIRouter, Response, status, HTTPException

from src.schemas import PayloadRequest, PayloadResponse
from src.utils.cache import generate_identifier, get_or_create_payload, get_payload_by_id
from src.core.database import DBSessionDep

router = APIRouter(prefix='/payload', tags=['Payload'])


@router.post("")
def create_payload_api(
    dbsession: DBSessionDep,
    response: Response,
    payload: PayloadRequest,
) -> PayloadResponse:
    identifier = generate_identifier(payload.list_1, payload.list_2)

    output, created = get_or_create_payload(
        session=dbsession,
        identifier=identifier,
        payload_request=payload
    )

    if created:
        response.status_code = status.HTTP_201_CREATED
    response.headers['X-Cached'] = '0' if created else '1'
    return output


@router.get("/{id}")
def retrieve_payload_api(session: DBSessionDep, id: str) -> PayloadResponse:
    payload = get_payload_by_id(session, id)
    if payload:
        return payload

    raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Payload not found')
