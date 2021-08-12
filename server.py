from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    total = int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    now = datetime.datetime.now().strftime("%m/%d/%Y, at %H:%M %p")
    print(f"Charging {request.form['first_name']} for {total} fruit")
    return render_template("checkout.html",total= total,now = now)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)