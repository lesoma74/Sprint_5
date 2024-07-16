import pytest
from test_setup import TestSetup

@pytest.fixture(scope="class")
def setup_teardown(request):
    setup = TestSetup()
    request.cls.setup = setup
    setup.setup_method()  # Инициализация
    yield
    setup.teardown_method()  # Очистка




