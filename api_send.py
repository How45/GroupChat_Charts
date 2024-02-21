"""Flask web module"""
import os
from flask import Flask, jsonify
import reader_scripts.whatsapp_reader as whatsApp
import graphs

app = Flask(__name__)

@app.route("/api/graphData", methods=['GET'])
def get_data():
    """
    API page for graph data
    """
    file_name = 'Not_LyfeRP_Chat.txt'
    upload_dir = os.path.join('.', 'file_upload',file_name)
    converter = whatsApp.WhatsAppReader(upload_dir)
    dataframe = converter.open_file()

    most_sent_messages = graphs.user_sent_message(dataframe)
    most_name_data = graphs.who_said_most_name(dataframe, ['joe','milly','julia'])
    word_count = graphs.plot_word_count(dataframe)
    name_said_most = graphs.name_said_most(dataframe, ['joe','milly','julia'])
    response_message = graphs.response_messsages(dataframe)

    return jsonify(most_sent_messages, most_name_data, word_count, name_said_most, response_message)

if __name__ == '__main__':
    app.run()
