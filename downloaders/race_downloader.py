from typing import Self
from .base_downloader import BaseDownloader
from .race_utilities import StateTypes

class RaceDownloader(BaseDownloader):
    def __init__(self: Self) -> None:
        super().__init__()
        self.states = []

    def _create_state_calendar_url(self: Self, state: StateTypes) -> str:
        return f'{self.base_url}/FreeFields/Calendar.aspx?State={state.upper()}'
    
    def download_state_calendar(self: Self, state: StateTypes) -> dict:
        url = self._create_state_calendar_url(state)
        soup = self._get_soup(url=url, request_type='GET')
        page_content = soup.find('div', {'id': 'page-content'})
        main_table = page_content.find('table', {'class': 'race-fields'})
        trs = main_table.find_all('tr')
        print(len(trs))