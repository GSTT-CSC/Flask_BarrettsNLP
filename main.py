from flask import Flask, make_response, request, render_template
import pandas as pd
from werkzeug.utils import secure_filename
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def form():
    return render_template('index.html')



@app.route('/barrPath', methods=["POST"])
def barrPath_view():
    if request.method == 'POST':
       # data_file is the name of the file upload field
       f = request.files['data_file']

       # for security - stops a hacker e.g. trying to overwrite system files
       filename = secure_filename(f.filename)

       # save a copy of the uploaded file
       f.save(filename)

       # And then use it ...
       df = pd.read_csv(filename)

       df.style.set_table_styles([{'selector': '',
                                   'props': [('border',
                                              '10px solid yellow')]}])

       return render_template('table_viewer.html',  tables=[df.to_html(classes='table table-striped')], titles=df.columns.values)
    return 'Oops, Try again something went wrong!'


@app.route('/barrPathPredict', methods=["POST"])
def barrPath_predict():
    #This is the part that should submit the curl request:
    if request.method == 'POST':


       return render_template('table_viewerPred.html')
    return 'Oops, Try again something went wrong!'




if __name__ == '__main__':
    app.run(debug=True)
