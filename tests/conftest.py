from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    """Keep tests isolated by restoring the in-memory activity state each time."""
    original_activities = deepcopy(activities)

    yield

    activities.clear()
    activities.update(deepcopy(original_activities))
