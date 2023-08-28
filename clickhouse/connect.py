from aioch import Client
from config.config import Settings
from fastapi.exceptions import HTTPException


class ClickHouseConnector:
    async def execute(self, query):
        try:
            client = Client(
                    host=Settings.CLICKHOUSE_HOST,
                    port=Settings.CLICKHOUSE_PORT,
                    database=Settings.CLICKHOUSE_DB,
                    user=Settings.CLICKHOUSE_USER,
                    password=Settings.CLICKHOUSE_PASSWORD
            )
            response = await client.execute(query)
            return response
        except Exception as e:
            raise HTTPException(401, detail=f"Error while connecting to ClickHouse: {e}")

db = ClickHouseConnector()
