"""Graph, numpy modules and helper function"""
import json
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import helper as hp

def plot_word_count(dataframe: pd.DataFrame) -> json:
    """
    Plots most popular words used (top 100)
    """
    dataframe['Message'] = dataframe['Message'].apply(hp.remove_stopwords)
    word_count = dataframe['Message'].str.split(expand=True).stack().value_counts()

    word_count_df = pd.DataFrame({'Word': word_count[:100].index, 'Count': word_count[:100].values})
    data = {str(row['Word']): int(row['Count']) for _, row in word_count_df[:100].iterrows()}

    return json.dumps(data)
    # plt.title("Top 100 words used")
    # plt.show()

def name_said_most(dataframe: pd.DataFrame, extra_names: list) -> json:
    """
    Most common name used
    """
    word_count = dataframe['Message'].str.split(expand=True).stack().value_counts()
    names = dataframe['User'].unique()
    if extra_names:
        names = np.append(names, extra_names)

    name_count = []
    place_holder = 0

    for name in names:
        if name in word_count:
            try:
                place_holder = word_count[name]
            except KeyError as k:
                print(f'Error: {k} - No {name} was found')
            name_count.append(place_holder)
        place_holder = 0

    data = {name.capitalize(): int(value) for name, value in zip(names, name_count)}
    return json.dumps(data)
    # print(name_count)
    # plt.bar([name.capitalize() for name in names], name_count)
    # plt.title("How often names have been said")
    # plt.show()

def user_sent_message(dataframe: pd.DataFrame) -> json:
    """
    How often a user has sent a message
    """
    names = dataframe['User'].unique()
    count_names = [dataframe[dataframe['User'] == name]['User'].count()
                   for name in names] # Count messages
    percent = [(i/sum(count_names))*100 for i in count_names]
    # Have everything as one name
    concat_name=[f'{name.capitalize()}, {perc:.{2}f}%'
                 for name, perc in zip(names,percent)]

    data = {name.capitalize(): int(value) for name, value in zip(concat_name, count_names)}
    return json.dumps(data)
    # plt.pie(count_names,labels=concat_name)
    # plt.title("Who sent the most messages")
    # plt.show()

def response_messsages(dataframe: pd.DataFrame) -> json:
    """
    Graph to see number of messages sent with no response (10 minutes)
    """
    names = dataframe['User'].unique()
    counts  = [hp.no_response(dataframe,names) for names in dataframe['User'].unique()]

    data = {name.capitalize(): count for name, count in zip(names,counts)}
    # print(data)
    return json.dumps(data)
    # plt.bar([name.capitalize() for name in names], count)
    # plt.title("Number of messages sent with no response (10 minutes)")
    # plt.show()

def who_said_most_name(dataframe: pd.DataFrame, names_to_check: list) -> json:
    """
    Graph to see who send who's name the most
    """
    users = dataframe['User'].unique()
    if names_to_check:
        names_to_check = np.append(users, names_to_check)
    else:
        names_to_check = users

    data = {user.capitalize():
                           hp.count_mentions(dataframe, user, names_to_check) for user in users}
    # dataframe_mentions = pd.DataFrame(data).T

    # print(data)
    return json.dumps(data)
    # dataframe_mentions.plot(kind='bar', stacked=True)
    # plt.title('User Mentions of Names')
    # plt.show()
