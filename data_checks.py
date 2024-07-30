"""
Unit testing program to test work
"""
# import json
import unittest
import reader_scripts.whatsapp_reader as whatsApp
# import reader_scripts.discord_reader as discord
import graphs
# import helper as hp


class TestApp(unittest.TestCase):
    """
    Unit-test class
    """
    def setUp(self):
        # Example file needs to be added
        whats_reader = whatsApp.WhatsAppReader('file_upload/Not_LyfeRP_Chat.txt')

        # Example file needs to be added
        # dis_reader = discord.DiscordReader('file_upload/messages.csv')

        self.whats_dataframe = whats_reader.open_file()
        # self.dis_dataframe = dis_reader.open_file()

    def test_dataframes(self):
        """
        Test dicord reader
        """
        # print(self.dis_dataframe.head())
        print(self.whats_dataframe.head())

    def test_response_graph(self):
        """
        Testing response_messsages graph
        """
        print(graphs.response_messsages(self.whats_dataframe))

    def test_convos(self):
        """
        Testing the convos_time
        """
        graphs.convos_time(self.whats_dataframe)

if __name__ == '__main__':
    unittest.main()
