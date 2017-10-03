from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/', methods = ['GET', 'POST'])
def root():
    return render_template('form.html') 

@my_app.route('/greet', methods = ['POST'])
def greet(): 
    print request.form['username']
    return render_template("greeting.html", input1 = request.form['username'], input2 = request.method)
 

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()

    
