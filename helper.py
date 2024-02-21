"""Time module"""
from datetime import datetime, timedelta
import pandas as pd
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
def remove_stopwords(text:str) -> str:
    """
    Remove stop words
    """
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def add_time(time: str) -> str:
    """
    Adds 10 minutes
    """
    time_obj = datetime.strptime(time, '%H:%M:%S')
    new_time_obj = time_obj + timedelta(minutes=10)
    new_time_str = new_time_obj.time().strftime('%H:%M:%S')
    return new_time_str

def to_pandas(log: list) -> pd.DataFrame:
    """
    Converst list to pandas
    """
    if log and log[0][0] != 'Date':
        log.insert(0,['Date','Time','User','Message'])
        dataframe = pd.DataFrame(log[1:],columns=log[0])
        return dataframe

def no_response(dataframe: pd.DataFrame, target_user: str) -> int:
    """
    How often does user send message and no one says anything after 10 minutes
    """
    data = []
    for date, time, user, message in zip(dataframe['Date'], dataframe['Time'],
                                         dataframe['User'],dataframe['Message']):
        if user == target_user:
            data.append([date, time, user, message])
        elif user != target_user:
            if data and time < add_time(data[-1][1]) and date == data[-1][0]:
                # If other user responds with in 10 minutes to target_users message
                data.pop()
        else:
            print(f"Statement either doesn't make sence or issue: {date} - {time} - {user}")
    dataframe = to_pandas(data)
    return int(len(dataframe.index))

def count_mentions(dataframe: pd.DataFrame, user: str, name_check: list) -> dict:
    """
    Counts the amount of times a name has been mentioned by user
    """
    mention_count = {name.capitalize(): 0 for name in name_check}
    user_messages = dataframe[dataframe['User'] == user]

    for name in name_check:
        try:
            mention_count[name.capitalize()] = int(user_messages['Message'].str.split(expand=True).stack().value_counts()[name])
        except KeyError:
            mention_count[name.capitalize()] = int(0)

    return mention_count
