import pytest


@pytest.fixture
def capsys():
    return CaptureFixture()
