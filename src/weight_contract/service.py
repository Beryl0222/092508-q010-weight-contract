"""减重训练承诺履约裁决的应用服务入口。"""
from .domain import Record
from .store import Store


class Service:
    def __init__(self, store: Store | None = None) -> None:
        self.store = store or Store()

    def health(self) -> dict[str, str]:
        return {"service": "weight_contract", "status": "ok"}

    def register(self, record_id: str, owner_id: str) -> dict[str, str | int]:
        saved = self.store.add(Record(record_id=record_id, owner_id=owner_id))
        return {
            "record_id": saved.record_id,
            "owner_id": saved.owner_id,
            "state": saved.state,
            "revision": saved.revision,
            "created_at": saved.created_at,
        }

    def find(self, record_id: str) -> dict[str, str | int] | None:
        record = self.store.get(record_id)
        return record.__dict__.copy() if record else None
