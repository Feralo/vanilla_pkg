from unittest.mock import Mock, patch
from nose.tools import assert_true, assert_is_not_none

from vanilla_pkg import get_todos

@patch('vanilla_pkg.Mocks.requests.get')
def test_request_response(mock_get):
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
