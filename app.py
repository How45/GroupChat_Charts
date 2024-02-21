"""Flask web module"""
import os
from flask import Flask, render_template, request # , redirect, url_for
from werkzeug.utils import secure_filename
import reader_scripts.whatsapp_reader as whatsApp
import graphs

app = Flask(__name__)

ALLOWED_EXTENTIONS = (['txt','json','csv'])

def allowed_file(filename):
    """
    Checks if its allowed
    """
    return '.' in filename and \
            filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS

@app.route("/", methods=['GET','POST'])
def file_drop():
    """
    page to drop chat file
    """
    if request.method == 'POST':
        file = request.files['chat-file']

        if file and allowed_file(file.filename):
            file_name = secure_filename(file.filename) # Removes '/'
            upload_dir = os.path.join('.', 'file_upload')

            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            file.save(os.path.join('file_upload', file_name))

        else:
            return "Incorrect file type" # redirect

    return render_template('file_drop.html', files=os.listdir('file_upload'))

@app.route("/display_graphs", methods=['GET','POST'])
def graph_display():
    """
    Where all the graphs are displayed
    """
    if request.method == 'POST': # Change Added list
        file_name = request.form.get('file_name')
        upload_dir = os.path.join('.', 'file_upload',file_name)

        converter = whatsApp.WhatsAppReader(upload_dir)
        dataframe = converter.open_file()

        return render_template('display_graphs.html',
                               most_sent_messages = graphs.user_sent_message(dataframe),
                               most_name_data = graphs.who_said_most_name(dataframe, ['joe','milly','julia']),
                               word_count = graphs.plot_word_count(dataframe),
                               name_said_most = graphs.name_said_most(dataframe, ['joe','milly','julia']),
                               response_message = graphs.response_messsages(dataframe))

if __name__ == '__main__':
    app.run()
