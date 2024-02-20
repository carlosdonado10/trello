from pydantic import ValidationError
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_KEY: str
    TOKEN: str

    def get_auth_query_params(self):
        return {
            'key': self.API_KEY,
            'token': self.TOKEN
        }


settings = Settings()
