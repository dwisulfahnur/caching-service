from typing import List

def transform_payload(list_1: List[str], list_2: List[str]) -> str:
    list_1_transformed = [item.upper() for item in list_1]
    list_2_transformed = [item.upper() for item in list_2]
    interleaved_output = ", ".join(
        [val for pair in zip(list_1_transformed, list_2_transformed) for val in pair]
    )
    return interleaved_output
