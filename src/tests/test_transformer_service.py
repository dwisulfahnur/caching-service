from src.services.transformer import transform_payload


def test_transformer_service():
    input_payload = {
        "list_1": ["first string", "second string", "third string"],
        "list_2": ["other string", "another string", "last string"]
    }
    transformed = transform_payload(
        list_1=input_payload['list_1'],
        list_2=input_payload['list_2']
    )
    assert transformed == "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING, THIRD STRING, LAST STRING"
