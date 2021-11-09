from flask import *
import os
from text import *

app=Flask(__name__)
app.config['SECRET_KEY']='text'

@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method == "POST":
       enter_text = request.form.get("texttotranslate")
       source_lang = request.form.get("sourcelang")
       target_lang = request.form.get("targetlang") 
       trans = translate_text(target=target_lang,text=enter_text)
       return render_template("display.html",data = trans)
    return render_template("index.html")