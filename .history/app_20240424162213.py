from flask import Flask, render_template, request, redirect
from auto_data_analysis import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/analysis', methods=['GET', 'POST'])
def data_analysis_automation():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('static/uploads', filename))
            data_analysis('/static/uploads/' + filename)
    return render_template('Data_analysis.html')

@app.route('/scraper/automation', methods=['GET', 'POST'])
def scraper_automation():
    if request.method == 'POST':
        print(request.form)
    return render_template('scraper_automation.html')

@app.route('/data/cleaning/automation', methods=['GET', 'POST'])
def data_cleaning_automation():
    if request.method == 'POST':
        print(request.form)
    return render_template('data_analysis.html')

@app.route('/database/maintenance/automation', methods=['GET', 'POST'])
def database_maintenance_automation():
    return render_template('database_maintenance.html')

@app.route('/email/sending/automation', methods=['GET', 'POST'])
def email_sending_automation():
    return render_template('email_sending.html')

@app.route('/file/automation', methods=['GET', 'POST'])
def file_automtion():
    return render_template('file_automation.html')

@app.route('/image/processing', methods=['GET', 'POST'])
def image_processing():
    return render_template('image_processing.html')
    
@app.route('/natural/language/processing', methods=['GET', 'POST'])
def natural_language_processing():
    return render_template('natural_language_processing.html')

@app.route('/pdf/manipulation', methods=['GET', 'POST'])
def pdf_manipulation():
        return render_template('pdf_maipulation.html')

@app.route('/report/generation', methods=['GET', 'POST'])
def report_generation():
    return render_template('report_generation.html')

@app.route('/social/mediaposting', methods=['GET', 'POST'])
def social_mediaposting():
        return render_template('social_mediaposting.html')

@app.route('/task/scheduling', methods=['GET', 'POST'])
def task_scheduling():
        return render_template('task_scheduling.html')

@app.route('/text/processing', methods=['GET', 'POST'])

def text_processing():
        return render_template('text_processing.html')

@app.route('/web/testing', methods=['GET', 'POST'])
def web_testing():
        return render_template('web_testing.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 