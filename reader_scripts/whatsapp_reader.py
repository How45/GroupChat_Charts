"""Pandas, datetime modules and files imports"""
from datetime import datetime
import pandas as pd
import helper as hp

class WhatsAppReader():
    """
    Converter whatapp data to pd
    """
    def __init__(self, file: str) -> None:
        self.file = file

    def clean_data(self, old_log: list) -> list:
        """
        Returns clean data as:
        [['date time user', text]]
        """
        old_log = [line for line in old_log if line != ''
                and ':' != line[-1] and 'created group' not in line]

        temp_log = [line.split(':',2) for line in old_log]

        try:
            log = []
            for line in temp_log:
                if len(line) > 2:
                    log.append([line[0] + ':' + line[1],line[2][1:]])
        except Exception as error:
            print(f"Error: {error} occurred at line: {line}")

        return log

    def normalise_data(self, old_log: list) -> list:
        """
        configuring data to be [date, time, user, text]
        """
        log = []
        for line in old_log:
            meta_data = line[0].split(' ')
            chat_date = datetime.strptime(meta_data[0][:-1], '%d/%m/%Y').date()
            chat_time = f'{meta_data[1]}:00'
            log.append([chat_date,chat_time,meta_data[3].lower(),line[1].lower()])
        return log

    def open_file(self) -> pd.DataFrame:
        """
        opens txt file
        """

        with open(self.file, encoding='utf-8') as text:
            chat_log = text.read()
        chat_log = chat_log.split('\n')

        log = self.clean_data(chat_log)
        log = self.normalise_data(log)
        dataframe = hp.to_pandas(log)

        dataframe.to_excel('LyfeRP_Chat.xlsx', index=False)
        # return dataframe
if __name__ == '__main__':
    wap = WhatsAppReader('Not_LyfeRP_Chat.txt')
    wap.open_file()
    