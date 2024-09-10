from secrets import token_urlsafe

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings as _BaseSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file="../.env", env_file_encoding="utf-8")


class CommonConfig(BaseSettings, env_prefix="COMMON_"):
    bot_token: SecretStr
    drop_pending_updates: bool
    admin_id: int


class PostgresConfig(BaseSettings, env_prefix="POSTGRES_"):
    host: str
    port: int
    user: str
    password: SecretStr
    db: str

    @property
    def dsn(self) -> str:
        return f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class WebhookConfig(BaseSettings, env_prefix="WEBHOOK_"):
    host: str
    port: int
    path: str
    base_url: str
    reset: bool

    secret_token: SecretStr = Field(default_factory=token_urlsafe)

    @property
    def full_url(self) -> str:
        return f"{self.base_url}{self.path}"


class AppConfig(BaseModel):
    common: CommonConfig
    postgres: PostgresConfig
    webhook: WebhookConfig
