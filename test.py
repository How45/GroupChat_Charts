"""
Unit testing program to test work
"""
# import json
import unittest
import reader_scripts.whatsapp_reader as whatsApp
import reader_scripts.discord_reader as discord
import graphs
# import helper as hp

class TestApp(unittest.TestCase):
    """
    Unit-test class
    """
    def setUp(self):
        whats_reader = whatsApp.WhatsAppReader('file_upload/WhatsApp_Chat_with_Not_LyfeRP.txt') # Example file needs to be added
        dis_reader   = discord.DiscordReader('file_upload/messages.csv') # Example file needs to be added
        self.whats_dataframe = whats_reader.open_file()
        self.dis_dataframe = dis_reader.open_file()
        self.names_to_check = ['joe','milly','julia','elliot']

    def test_dataframes(self):
        """
        Test dicord reader
        """
        print(self.dis_dataframe.head())
        print(self.whats_dataframe.head())

    def test_response_graph(self):
        """
        Testing response_messsages graph
        """
        print(graphs.response_messsages(self.dis_dataframe))

if __name__ == '__main__':
    unittest.main()
