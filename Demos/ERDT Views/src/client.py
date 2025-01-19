from typing import Type, TypeVar
import requests

T = TypeVar("T")


class DittoClient:
    def query(self, return_type: Type[T]) -> list[T]:
        response = requests.get(
            "https://ditto.eclipseprojects.io/api/2/search/things?namespaces=com.erdt.test2",
            headers={
                "accept": "application/json",
                "Authorization": "Basic ZGl0dG86ZGl0dG8=",
            },
        )
        return [return_type.from_ditto(item) for item in response.json()["items"]]