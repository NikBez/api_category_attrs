from clickhouse_driver import Client

from config.config import Settings


class ClickHouseConnector:
    def connect(self):
        try:
            with Client(
                    host=Settings.CLICKHOUSE_HOST,
                    port=Settings.CLICKHOUSE_PORT,
                    database=Settings.CLICKHOUSE_DB,
                    user=Settings.CLICKHOUSE_USER,
                    password=Settings.CLICKHOUSE_PASSWORD
            ) as client:
                return client
        except Exception as e:
            print(f"Error connecting to ClickHouse: {e}")
            return None

db = ClickHouseConnector()
