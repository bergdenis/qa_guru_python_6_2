import pytest


@pytest.fixture(scope="session")
def browser():
    print("Браузер стартует")
    yield
    print("Браузер закрывается")


@pytest.fixture
def chrome(browser):
    pass


@pytest.fixture(scope="module")
def user_id():
    return 123


def test_auth(user_id, chrome):
    assert user_id == 123


def test_second(user_id, chrome):
    assert user_id == 123
