from unittest.mock import Mock, patch
from nose.tools import assert_true, assert_is_none, assert_is_not_none

from vanilla_pkg import get_todos


@patch("vanilla_pkg.Mocks.requests.get")
def test_request_response(mock_get):
    mock_get.return_value.ok = True
    response = get_todos()
    assert_is_not_none(response)

@patch("vanilla_pkg.Mocks.requests.get")
def test_request_response_not_ok(mock_get):
    mock_get.return_value.ok = False
    response = get_todos()
    assert_is_none(response)
