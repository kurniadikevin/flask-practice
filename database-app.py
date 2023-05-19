from flask import Flask, redirect, url_for, request, render_template
import sqlite3
app = Flask(__name__)


@app.route('/enternew')
def new_student():
   return render_template('database-app.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("database-app-result.html",msg = msg)
         con.close()

#Read data
@app.route('/list')
def list():
   con = sqlite3.connect("database.db")
   con.row_factory = sqlite3.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   return render_template("database-app-list.html",rows = rows)

#home
@app.route('/')
def home():
   return render_template('database-app-home.html')

if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)