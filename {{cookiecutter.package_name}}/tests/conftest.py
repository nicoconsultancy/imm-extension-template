import pytest


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    # enough of the tests use the database that we can enable it for all of them
    pass
