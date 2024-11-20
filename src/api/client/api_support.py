class ApiSupport:
    """A helper class for working with API responses and validating their content."""

    def __init__(self, api):
        self.api = api

    def get_response_body(self):
        """Navigate the web driver to the specified URL."""
        json_response = self.api.response.json()
        return json_response

    def check_response_headers(self, key: str, value: str):
        """
        Validates that a specific header in the response matches the expected value.

        Args:
            key (str): The header key to check.
            value (str): The expected value for the header.
        """
        response = self.api.response
        assert response.headers[key] == value, (
            f'"Expected header with key={key}, value={value}, '
            f"got {response.headers[key]}"
        )

    def get_response_value(self, field_name: str):
        """
        Retrieve the value of a specified field from the JSON response.

        Args:
            field_name (str): The name of the field to retrieve from the JSON response.
        Returns:
            The value associated with the specified field name in the JSON response.
        """
        json_response = self.get_response_body()
        return json_response[field_name]

    def validate_response_attribute_equals(self, field_name: str, expected_value: str):
        """
        Validate that the specified field in the JSON response matches the expected value.

        Args:
            field_name (str): The name of the field to retrieve from the JSON response.
            expected_value (Any): The value expected for the specified field.
        """
        value = self.get_response_value(field_name)
        assert str(value) == str(
            expected_value
        ), f"Expected value: {expected_value}, got: {value}"

    def check_status_code(self, name: str = None, expect_code: int = 200):
        """
        Check if the HTTP response status code matches the expected status code.

        Args:
            name (str, optional): A label for the request being checked, used in error messages.
            expect_code (int, optional): The expected HTTP status code. Defaults to 200.
        """
        actual_code = self.api.response.status_code
        assert actual_code == expect_code, (
            f"Request for {name} failed.\n"
            f"Request URL: {self.api.response.request.method}"
            f":{self.api.response.request.url}\n"
            f"Request body: {self.api.response.request.body}\n"
            f"Expected status code: {expect_code}\n"
            f"Actual status code: {actual_code}\n"
            f"Reason: {self.api.response.reason}\n"
            f"Text: {self.api.response.text}"
        )
