from pymongo.collection import Collection


class ApiClient:
    def __init__(self, message_collection: Collection):
        self.message_collection = message_collection

    def get_message(self, message_id: str) -> str:
        result = self.message_collection.find_one({"message_id": message_id})
        return result.get("message")
