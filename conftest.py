import pytest
from helpers import *


@pytest.fixture(scope='function')
def create_user():
    login_pass = registration_user()
    yield login_pass
    delete_user()

