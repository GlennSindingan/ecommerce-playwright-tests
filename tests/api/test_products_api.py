from pygments.lexers import data
from api.clients.products_api import ProductsAPI
from pprint import pprint


def test_get_all_products():
    products_api = ProductsAPI()
    response = products_api.get_all_products()
    assert response.status_code == 200

    data = response.json()

    assert data["responseCode"] == 200
    assert "products" in data
    assert len(data["products"]) > 0

    pprint(data["products"][:3])

def test_post_product_negative():
    products_api = ProductsAPI()
    response = products_api.post_product_negative()

    assert response.status_code == 200

    data = response.json()

    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."

def test_all_brand_list():
    products_api = ProductsAPI()

    response = products_api.get_brand_list()
    assert response.status_code == 200

    data = response.json()

    assert len(data["brands"]) > 0
    assert data["responseCode"] == 200
    pprint(data)

def test_post_brand_negative():
    products_api = ProductsAPI()

    response = products_api.post_brand_negative()
    assert response.status_code == 200

    print(response.status_code)
    print(response.text)

    data = response.json()

    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."

def test_search_product():
    products_api = ProductsAPI()

    response = products_api.post_search_product("top")
    assert response.status_code == 200

    pprint(response.text)

    data = response.json()

    assert data["responseCode"] == 200



