"""Pandas, datetime modules and files imports"""
import pandas as pd

class DiscordReader():
    """
    Class for discord script reader
    """
    def __init__(self, file: str) -> None:
        self.file = file

    def rename_id(self, id_number: pd.Series) -> pd.Series:
        """
        Replaces id number to names of users
        """
        id_name = { # Will need to change this!!!!!!!!!!
            326065900488753174: 'Max',
            230768420604477440: 'Joseph',
            510890598610501643: 'Sam',
            252834508917833729: 'Angus',
            423119927336108042: 'Luna',
            493498291217235969: 'Issy',
            331849718160293890: 'Chloe',
            511942965749350423: 'Sophie',
            184405311681986560: 'MusicSurf'
        }
        return id_number.map(id_name)

    def time_norm(self, value: str) -> pd.Timestamp:
        """
        Converts time column
        """
        try:
            value = value.split('.')[0]
            value = value.split('+')[0]
            return pd.to_datetime(value, format="%Y-%m-%d %H:%M:%S",errors='coerce')

        except ValueError as vale_error:
            print(vale_error)
            return None

    def normalise_date(self, timestamp: pd.Series) -> pd.DataFrame:
        """
        configuring timestamp to date, time and Splits the date and time into two different columns
        """
        timestamp = [self.time_norm(value) for value in timestamp]
        datetime_dataframe = pd.DataFrame()
        datetime_dataframe['Date'] = [d.date() for d in timestamp]
        datetime_dataframe['Time'] = [d.time() for d in timestamp]

        return datetime_dataframe

    def open_file(self) -> pd.DataFrame:
        """
        opens txt file
        """
        dataframe = pd.read_csv(self.file)
        # dataframe['ID'] = rename_id(dataframe['ID'])
        dataframe['Contents'] = dataframe['Contents'].astype(str).str.lower()

        datetime_dataframe = self.normalise_date(dataframe['Timestamp'])
        dataframe.drop(columns=['Timestamp'], inplace=True)
        dataframe = pd.concat([dataframe, datetime_dataframe], axis=1)
        dataframe.rename(columns={'ID':'User',
                                  'Contents':'Message',
                                  'Attachments':'Attachments',
                                  'Date':'Date','Time':'Time'}, inplace=True)

        return dataframe
