import time
import random
from typing import List

def transform_payload(list_1: List[str], list_2: List[str]) -> str:
    """
    Transforms two lists of strings by converting each string to uppercase and interleaving the 
    transformed lists into a single comma-separated string. This function simulates an external 
    service by introducing a random delay between 300ms and 1200ms.

    Args:
        list_1 (List[str]): The first list of strings to transform.
        list_2 (List[str]): The second list of strings to transform.

    Returns:
        str: A comma-separated string with interleaved elements from `list_1` and `list_2`, 
             both transformed to uppercase.
    """
    time.sleep(random.randint(300, 1500) / 1000)
    list_1_transformed = [item.upper() for item in list_1]
    list_2_transformed = [item.upper() for item in list_2]
    interleaved_output = ", ".join(
        [val for pair in zip(list_1_transformed, list_2_transformed) for val in pair]
    )
    return interleaved_output
