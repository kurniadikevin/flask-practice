from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_flask():
   return 'Hello python flask!'

@app.route('/hello')
def hello_world():
   return 'hello world'

@app.route('/hello/<string:text>/')
def hello_params(text):
   return f"hello {text}"

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return f'Hello {guest} as Guest'

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

# Login sample
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login-page')
def displayLogin():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      if user == 'admin':
         return redirect(url_for('success',name = 'As admin mode'))
      else:
         return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
   
#trying out template ( templates folder is special folder for templates/ view file)
@app.route('/template/<name>')
def index(name):
   return render_template('hello.html', name = name)

# Sample for conditional on templates page 
@app.route('/test-score/<int:score>')
def hello_name(score):
   return render_template('test-score.html', marks = score)

# Sample for loop/ mapping on templates page
@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

# Sample for static with js
# file for js function stored on static folder ( special name folder like templates)
@app.route("/static")
def clickMe():
   return render_template("index.html")


if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)