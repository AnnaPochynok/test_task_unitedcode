import pytest

from src.api.client.api_support import ApiSupport
from src.api.features.image_api import ImageApi
from data import constants


@pytest.mark.usefixtures("api")
class TestApiCatsImage:

    @pytest.fixture(autouse=True)
    def pre_test(self, api):
        self.api = api
        self.img_api = ImageApi(api)
        self.support = ApiSupport(api)

    def test_get_random_cats_image(self):
        self.img_api.get_random_cats_image()
        self.support.check_status_code(expect_code=200)
        self.img_api.check_images_number_in_response(number=1)

    def test_get_eleven_images(self):
        self.img_api.get_images_list_with_limit(limit=11)
        self.support.check_status_code(expect_code=200)
        self.img_api.check_images_number_in_response(number=11)

    def test_get_image_by_id(self):
        self.img_api.get_cats_image_by_id(img_id=constants.TEST_IMAGE["id"])
        self.support.check_status_code(expect_code=200)
        self.support.validate_response_attribute_equals(
            field_name="id", expected_value=constants.TEST_IMAGE["id"]
        )
        self.support.validate_response_attribute_equals(
            field_name="url", expected_value=constants.TEST_IMAGE["link"]
        )

    def test_all_images_have_url(self):
        self.img_api.get_images_list_with_limit(limit=10)
        self.support.check_status_code(expect_code=200)
        self.img_api.check_all_images_have_url()

    def test_random_image(self):
        img_url = self.img_api.get_random_cat_img_url()
        self.img_api.get_cats_image_link(link=img_url)
        self.support.check_status_code(expect_code=200)
        self.support.check_response_headers(key="Content-Type", value="image/jpeg")
