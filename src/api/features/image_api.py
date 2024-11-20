from src.api.client.api_support import ApiSupport


class ImageApi:
    """
    A class to interact with the API for retrieving and validating images,
    specifically cat images.
    """

    def __init__(self, api):
        self.api = api
        self.support = ApiSupport(api)
        self.images_endpoint = "/images"
        self.search_endpoint = "/search"

    def get_random_cats_image(self):
        """Makes a GET request to retrieve a random cat image."""
        self.api.get(
            url=self.api.api_url,
            endpoint=f"{self.images_endpoint}{self.search_endpoint}",
        )

    def get_cats_image_by_id(self, img_id: str):
        """
        Retrieves a specific cat image by its ID.

        Args:
            img_id: The unique identifier of the image.
        """
        self.api.get(url=self.api.api_url, endpoint=f"{self.images_endpoint}/{img_id}")

    def get_random_cat_img_url(self):
        """
        Retrieves the URL of a random cat image.

        Returns:
            str: The URL of the cat image in the response.
        """
        self.api.get(
            url=self.api.api_url,
            endpoint=f"{self.images_endpoint}{self.search_endpoint}",
        )
        return self.support.get_response_body()[0]["url"]

    def get_images_list_with_limit(self, limit: int):
        """
        Retrieves a list of cat images with a specified limit.

        Args:
            limit: The maximum number of images to retrieve.
        """
        self.api.get(
            url=self.api.api_url,
            endpoint=f"{self.images_endpoint}{self.search_endpoint}",
            params=f"limit={limit}",
        )

    def get_cats_image_link(self, link: str):
        """
        Makes a GET request to retrieve a cat image using a direct link.

        Args:
            link: The direct URL of the image to retrieve.
        """
        self.api.get(url=link, endpoint="")

    def check_images_number_in_response(self, number: int):
        """
        Verifies that the number of images in the response matches the expected count.

        Args:
            number: The expected number of images.
        """
        cats_list = self.support.get_response_body()
        number_of_cats = len(cats_list)
        assert (
            number_of_cats == number
        ), f"Expected number of cats in the list: {number}, got {number_of_cats}"

    def check_all_images_have_url(self):
        """Validates that all images in the response have a valid URL with a supported format."""
        img_list = self.support.get_response_body()
        for i in img_list:
            url = i["url"]
            assert any(
                ext in url for ext in (".jpg", ".png", ".gif")
            ), f"Url is invalid: {url}"
