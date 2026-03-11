import requests
from utils.config import BASE_URL
from utils.logger import get_logger

logger = get_logger()


class APIClient:

    @staticmethod
    def get(endpoint):

        url = f"{BASE_URL}{endpoint}"

        logger.info(f"GET {url}")

        response = requests.get(url)

        logger.info(f"Status Code: {response.status_code}")

        return response


    @staticmethod
    def post(endpoint, payload=None):

        url = f"{BASE_URL}{endpoint}"

        logger.info(f"POST {url}")
        logger.info(f"Payload: {payload}")

        response = requests.post(url, json=payload)

        logger.info(f"Status Code: {response.status_code}")

        return response