from flask import *  
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './media'
  
@app.route('/')  
def main():  
    return render_template("index.html")  
  
@app.route('/upload', methods = ['POST'])  
def upload():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        return render_template("Acknowledgement.html", name = f.filename)




if __name__ == '__main__':  
    app.run(debug=True)
