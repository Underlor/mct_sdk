import requests
from requests import Response


class MctClient:
    def __init__(self, key: str, base_url='https://mc-t.ru/api/'):
        self.base_url = base_url
        self.session = requests.Session()
        self.key = key

    def send_post(self, method: str, kwargs: dict) -> Response:
        """
        Метод запроса к апи

        :param method: наименование метода
        :param kwargs: данные для метода
        """

        data = {
            'key': self.key,
            'method': method,
            'kwargs': kwargs
        }

        return self.session.post(f'{self.base_url}', json=data)

    def get_votes(self, days: int = 30) -> dict:
        """
        Метод получает количество голосов вашего проекта за промежуток времени

        :param days: Временной промежуток в днях
        """
        return self.send_post('getVotes', {'days': days, }).json()

    def send_vote_status(self, session_id: str) -> dict:
        """
        Метод получает количество голосов вашего проекта за промежуток времени

        """
        return self.send_post('sendVoteStatus', {'session_id': session_id, }).json()

    def echo(self, message: str) -> dict:
        """
        Метод метод для проверки доступности API
        """
        return self.send_post('getEcho', {'msg': message, }).json()

    def get_all_methods(self) -> dict:
        """
        Получение всех методов API
        """
        return self.send_post('getAllMethods', {}).json()
