from ._base import BaseAPI

from typing import Any
import json


class WasmAPI(BaseAPI):
    async def code_info(self, code_id: int) -> dict:
        return await self._c._get(f"/wasm/codes/{code_id}")

    async def contract_info(self, contract_address: str) -> dict:
        res = await self._c._get(f"/wasm/contracts/{contract_address}")
        return res

    async def contract_query(self, contract_address: str, query: dict) -> Any:
        params = {"query_msg": json.dumps(query)}
        return await self._c._get(f"/wasm/contracts/{contract_address}/{store}", params)

    async def parameters(self) -> dict:
        return await self._c._get(f"/wasm/parameters")
