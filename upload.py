from flask import Flask, render_template, request

#from werkzeug import secure_filename
#cannot import werkzeug

app = Flask(__name__)
	

@app.route('/upload')
def upload_index():
   return render_template('upload.html')

	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return f'file uploaded successfully {f.filename}'
		
if __name__ == '__main__':
   app.run(debug = True)