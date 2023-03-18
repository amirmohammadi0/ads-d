from flask import *  
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './media'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#----------------------------------------------------------------------
#views

@app.route('/')  
def main():  
    return render_template("index.html")  
  
@app.route('/upload', methods = ['POST'])  
def upload():  
    if request.method == 'POST':  
        f = request.files['file']
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return render_template("Acknowledgement.html", name = f.filename)




if __name__ == '__main__':  
    app.run(debug=True)
