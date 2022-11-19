import pytest

import os

# import json

# Import the fuctional fixtures as a plugin
# Note: fixtures with session scope need to be local

pytest_plugins = ["dbt.tests.fixtures.project"]


# The profile dictionary, used to write out profiles.yml
@pytest.fixture(scope="class")
def dbt_profile_target():
    return {
        "type": "sybaseiq",
        "threads": 1,
        "host": "localhost",
        "username": "dba",
        "password": "sql",
        "database": "demo",
    }
