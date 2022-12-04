#%%
import requests as r
import re
import __main__


class AoC:
    """Handles the reading of daily input data from AoC and writing it to file in the `inputs` folder."""

    # Check for and read session key from file
    try:
        with open('session') as session_file:
            session = session_file.readline()
            session = session.strip()
    except FileNotFoundError:
        raise Exception("Your repository is missing your session file.")

    def __init__(self):
        self.day = self.__get_day()
        self.get_input_file()

    def __get_day(self):
        """Gets day from `__main__` filename. Defaults to 1 if not located."""
        
        if __name__ != '__main__':
            file_name = __main__.__file__
            day = re.findall('.*day([0-9]*).py', file_name)[0]
        else:
            print("Day not found in file name, defaulting to 1")
            day = 1
        
        return day

    def get_input_file(self):
        url = f"https://adventofcode.com/2022/day/{self.day}/input"

        try:
            with open(f'inputs/input{self.day}.txt', mode='x') as input_file:
                response= r.get(url, headers={'Cookie':f'session={AoC.session}'})
                input_file.write(response.text)
        except FileExistsError:
            print(f"Input file for day{self.day} already exists, delete it if you'd like to refresh.")
        
if __name__ == '__main__':
    test = AoC()