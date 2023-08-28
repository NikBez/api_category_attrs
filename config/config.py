from environs import Env

env = Env()
env.read_env()

class Settings:
    CLICKHOUSE_HOST = env('CLICKHOUSE_HOST')
    CLICKHOUSE_PORT = env('CLICKHOUSE_PORT')
    CLICKHOUSE_USER = env('CLICKHOUSE_USER')
    CLICKHOUSE_PASSWORD = env('CLICKHOUSE_PASSWORD')
    CLICKHOUSE_DB = env('CLICKHOUSE_DB')


