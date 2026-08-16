import time
import pytest

@pytest.fixture
def dynamic_email():
    return f"test_user_{int(time.time())}@gmail.com"


@pytest.fixture
def page(context):
    page = context.new_page()

    page.route("**/*google-analytics.com/**", lambda route: route.abort())
    page.route("**/*googlesyndication.com/**", lambda route: route.abort())
    page.route("**/*googleadservices.com/**", lambda route: route.abort())

    yield page
    page.close()