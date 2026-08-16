import requests
from api.config import BASE_URL

class ProductsAPI:

    def get_all_products(self):
        return requests.get(f"{BASE_URL}/productsList")

    def post_product_negative(self):
        return requests.post(f"{BASE_URL}/productsList")

    def get_brand_list(self):
        return requests.get(f"{BASE_URL}/brandsList")

    def post_brand_negative(self):
        return requests.post(f"{BASE_URL}/brandsList")

    def post_search_product(self, product):
        payload = {
            "search_product": product,
        }
        response = requests.post(
            f"{BASE_URL}/searchProduct",
            data=payload
        )
        return response

