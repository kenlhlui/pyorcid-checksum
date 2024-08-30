#!/usr/bin/env python3
import re

class ORCID_Checksum:
    """Class to check the checksum of an ORCID ID

    Attributes:
    None
    """

    def __init__(self):
        pass

    def parse_orcid(self, orcid) -> str:
        """Function to parse the ORCID from the HTTPS URI format to the 16-digit number format

        Args:
            orcid (str): The ORCID in HTTPS URI with the 16-digit number

        Returns:
            str: The ORCID iD in 16-digit number, or None if the ORCID input is incorrect
        """
        # Check if the ORCID is in the URL format, and extract the ORCID ID
        if re.match(r"^https://orcid\.org/\d{4}-\d{4}-\d{4}-\d{3}[0-9X]{1}$", orcid):
            orcid = orcid.split("/")[-1]

        # Check if the ORCID iD is in correct ID format
        if re.match(r"^\d{4}-\d{4}-\d{4}-\d{3}[0-9X]{1}$", orcid):
            return orcid
        else:
            return None

    def check_orcid_checksum(self, orcid) -> bool:
        """Function to run the ORCID checksum checker

        Args:
            orcid (str): The ORCID ID in URL format or ID format

        Returns:
            bool: True if the ORCID checksum is correct, False if the ORCID checksum is incorrect
        """

        orcid = self.parse_orcid(orcid) # Parse the ORCID to the 16-digit number format
        if not orcid:
            return False
        else:
            # Extract the base digits from the ORCID, replace 'X' with 10, and convert to a list
            base_digits: str = orcid.replace("-", "")
            base_digits_list: list = [i for i in base_digits]
            base_digits_list: list[str] = [digit if digit != "X" else "10" for digit in base_digits]

            # Calculate the ORCID checksum
            total: int = 0
            for i in base_digits_list:
                total = (total + int(i)) * 2
            result: int = (12 - (total % 11)) % 11
            return True if result == 10 else False
