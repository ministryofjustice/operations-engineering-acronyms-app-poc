import os
from types import SimpleNamespace


def __get_env_var(name: str) -> str | None:
    return os.getenv(name)


app_config = SimpleNamespace(
    flask=SimpleNamespace(
        app_secret_key=__get_env_var("APP_SECRET_KEY"),
    ),
    logging_level=__get_env_var("LOGGING_LEVEL"),
    sentry=SimpleNamespace(
        dsn_key=__get_env_var("SENTRY_DSN_KEY"), environment=__get_env_var("SENTRY_ENV")
    ),
     postgres=SimpleNamespace(
        user=__get_env_var("POSTGRES_USER"),
        password=__get_env_var("POSTGRES_PASSWORD"),
        db=__get_env_var("POSTGRES_DB"),
        host=__get_env_var("POSTGRES_HOST"),
        port=__get_env_var("POSTGRES_PORT"),
        sql_alchemy_database_url=(
            f"postgresql://{__get_env_var('POSTGRES_USER')}:{__get_env_var('POSTGRES_PASSWORD')}@"
            f"{__get_env_var('POSTGRES_HOST')}:{__get_env_var('POSTGRES_PORT')}/{__get_env_var('POSTGRES_DB')}"
        )
    ),
     
)
