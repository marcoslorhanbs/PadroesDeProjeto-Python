from unittest.mock import MagicMock, call

from api_client import ApiClient


class TestApiClient:
    def test_get_message_should_return_correct_message(self):
        mock_collection = MagicMock()
        mock_collection.find_one.return_value = {
            "message_id": "some_id",
            "message": "some_message",
        }

        api_client = ApiClient(message_collection=mock_collection)
        message = api_client.get_message(message_id="some_id")

        assert message == "some_message"

    def test_get_message_should_call_find_one_on_mongo_client_correctly(self):
        mock_collection = MagicMock()

        api_client = ApiClient(message_collection=mock_collection)
        api_client.get_message(message_id="some_id")

        assert mock_collection.find_one.call_count == 1
        assert mock_collection.find_one.call_args == call({"message_id": "some_id"})
