import time
import pytest

@pytest.fixture
def dynamic_email():
    return f"test_user_{int(time.time())}@gmail.com"