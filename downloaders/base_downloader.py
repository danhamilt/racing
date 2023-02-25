from typing import Callable
import requests
from requests import Session, Request
from bs4 import BeautifulSoup as Soup
from .race_utilities import RequestTypes

class BaseDownloader:
    def __init__(self) -> None:
        self.base_url: str = 'https://racingaustralia.horse/'
        self.session: Session= requests.session()

    # TODO: wrap all requests and add retries
    def _get(self, url: str, params: dict = {}) -> Request:
        return self.session.get(url=url, params=params)
    
    def _post(self, url: str, params: dict = {}) -> Request:
        return self.session.get(url=url, post_data=params)
    
    def _get_request_type(self, request_type: RequestTypes) -> Callable:
        try:
            func = getattr(self, f'_{request_type.lower()}')
        except AttributeError:
            raise NotImplementedError(f"Method {request_type} for BaseDownloader not implemented")
        else:
            return func
        
    def _get_soup(self, url: str, request_type: RequestTypes, params: dict = {}) -> Soup:
        r = self._get_request_type(request_type)(url=url, params=params)
        return Soup(r.text, 'lxml')
    
    def _get_json(self, url: str, request_type: RequestTypes, params: dict = {}) -> Soup:
        r = self._get_request_type(request_type)(url=url, params=params)
        # TODO: wrap this for errors
        return r.json()
