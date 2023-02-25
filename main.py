from downloaders.race_downloader import RaceDownloader

def main():
    state = 'vic'
    rd = RaceDownloader()
    print(f"Getting race calendar for {state}")
    print("Number of rows in table")
    rd.download_state_calendar(state)

if __name__ == '__main__':
    main()