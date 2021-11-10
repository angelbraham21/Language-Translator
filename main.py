from flask import *
import os
from detect_labels import *

app=Flask(__name__)
app.config['SECRET_KEY']='text'
app.config['UPLOAD_FOLDER']="C:/Users/ANGEL ABRAHAM/Desktop/project/Image"
@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method == "POST":
       file=request.files['file']
       file_loc=os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
       file.save(file_loc)
       res=detect_labels(file_loc)
       return render_template("display.html",data = res)
    return render_template("index.html")