from flask import Flask, render_template, request, redirect, send_file
from auto_data_analysis import *
from werkzeug.utils import secure_filename
from auto_scraper_automation import *
from auto_data_cleaning import *
import os
from auto_image_processing import *
from auto_file_automation import *

app = Flask(__name__)
 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/analysis', methods=['GET', 'POST'])
def data_analysis_automation():
    if request.method == 'POST':
        files = request.files.getlist('files')
        print(files)
        for file in files:
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join('static/uploads', filename))
                print(f'File saved: {filename}')
        
        results = launch_data_analysis([f'static/uploads/{file.filename}' for file in files])
        base_url = 'http://127.0.0.1:8000/'
        return render_template('data_analysis_results.html', results=results, base_url=base_url)
    return render_template('data_analysis.html')

@app.route('/scraper/automation', methods=['GET', 'POST'])
def scraper_automation():
    if request.method == 'POST':
        print(request.form)
        websites = request.form['desc'].splitlines()
        selection = request.form['select']
        if selection == 'Single Page Scraper':
            results = single_page_scraper(websites)

            return render_template('scraper_automation.html', results=results, type='1')
        elif selection == 'Link Extractor':
            results = link_extractor(websites)
            return render_template('scraper_automation.html', results=results, type='2')
    return render_template('scraper_automation.html')

@app.route('/data/cleaning/automation', methods=['GET', 'POST'])
def data_cleaning_automation():
    if request.method == 'POST':
        print(request.form)
        files = request.files.getlist('files')
        tasks = request.form.getlist('task')
        tasks = [int(task) for task in tasks] # Convert to integer
        uploads = []
        print(f'uploaded files: {files}')
        for file in files:
            if file.filename:
                filename = secure_filename(file.filename)
                file.save(os.path.join('static/uploads', filename))
                uploads.append(f'static/uploads/{filename}')
                print(f'File saved: {filename}')
            else:
                print(f'skip {file.filename}') 
        results = automate_cleaning(uploads, tasks)
        df_tables = []
        for idx,result in enumerate(results):
            df = pd.read_csv(result, nrows=30)
            df_tables.append({
                'filename': os.path.basename(result),
                'table': df.to_html(classes='table table-bordered table-striped table-hover'),
                'path': result,
                'id': idx,
            })

        return render_template('data_cleaning.html', df_tables=df_tables)
                
    return render_template('data_cleaning.html')

@app.route('/file/automation', methods=['GET', 'POST'])
def file_automtion():
    if request.method == 'POST':
        task = request.form['task']
        files = request.files.getlist('files')
        if os.path.exists('static/filetask'):
             # delete it
             shutil.rmtree('static/filetask')
        os.makedirs('static/filetask', exist_ok=True)
        # upload files
        for file in files:
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join('static/filetask', filename))
        if task == 'rename':
            suffix = request.form['suffix']
            filetype = request.form['filetype']
            dst = 'static/completed_task'
            if os.path.exists(dst):
                shutil.rmtree(dst)
            os.makedirs(dst, exist_ok=True)
            src = 'static/filetask'
            result = rename_files_and_store_in_zip(src, dst, suffix, filetype)
            if result['status'] == 'success':
                 return send_file(result['path'], as_attachment=True)
            else:
                return render_template('file_automation.html', message=result['message'])
        if task == 'segregate':
            result = segregate_files_by_extension('static/filetask')
            if result['status'] == 'success':
                return send_file(result['path'], as_attachment=True)
            else:
                return render_template('file_automation.html', message=result['message'])
    return render_template('file_automation.html')

@app.route('/image/processing', methods=['GET', 'POST'])
def image_processing():
    if request.method == 'POST':
        files = request.files.getlist('folder')
        w = request.form.get('width', 200)
        h = request.form.get('height', 200)
        format = request.form.get('format', 'png')
        filter = request.form.get('filter', 'b/w')
        print(f'files: {files}')
        for file in files:
            if file:
                if os.path.exists('static/image_task'):
                    shutil.rmtree('static/image_task')
                os.makedirs('static/image_task', exist_ok=True)
                filename = secure_filename(file.filename)
                file.save(os.path.join('static/image_task', filename))
                print(f'File saved: {filename}')
            else:
                print(f'skip {file.filename}')
        # result = resize_images('static/image_task', size=(int(w), int(h)), filter=filter, format=format)
        # return send_file(result, as_attachment=True)
    return render_template('image_processing.html')
    
@app.route('/database/maintenance/automation', methods=['GET', 'POST'])
def database_maintenance_automation():
    return render_template('coming_soon.html')

@app.route('/email/sending', methods=['GET', 'POST'])
def email_sending_automation():
    return render_template('coming_soon.html')

@app.route('/natural/language/processing', methods=['GET', 'POST'])
def natural_language_processing():
    return render_template('coming_soon.html')

@app.route('/pdf/manipulation', methods=['GET', 'POST'])
def pdf_manipulation():
    return render_template('coming_soon.html')

@app.route('/report/generation', methods=['GET', 'POST'])
def report_generation():
    return render_template('coming_soon.html')

@app.route('/task/scheduling', methods=['GET', 'POST'])
def task_scheduling():
    return render_template('coming_soon.html')

@app.route('/text/processing', methods=['GET', 'POST'])
def text_processing():
    return render_template('coming_soon.html')


# link would be like 
@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    path = os.path.join('static/cleaned_data', filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 