import json
import unittest

from weight_contract.api import handle
from weight_contract.service import Service
from weight_contract.store import Store


class 基础行为测试(unittest.TestCase):
    def test_health(self):
        result = json.loads(handle('{"action":"health"}', Service(Store())))
        self.assertEqual(result["status"], "ok")

    def test_register_and_find(self):
        service = Service(Store())
        created = service.register("record-1", "owner-1")
        self.assertEqual(created["state"], "draft")
        self.assertEqual(created["revision"], 1)
        self.assertEqual(service.find("record-1")["owner_id"], "owner-1")


if __name__ == "__main__":
    unittest.main()
