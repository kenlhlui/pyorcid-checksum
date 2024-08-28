"""Test the ORCID_Checksum class in the checksum module
"""
from src.checksum import ORCID_Checksum
import json
import pytest

# Load the ORCID test data
with open("tests/data/orcid_test_data.json", encoding="utf-8") as f:
    ORCID_DICT = json.load(f)

@pytest.mark.parametrize("key, value", ORCID_DICT.items())
def test_orcid_checker(key, value):
    """Test the orcid_checker function in the ORCID_Checksum class"""
    orcid = ORCID_Checksum()
    assert orcid.check_orcid_checksum(value["value"]) == value["is_correct"]
