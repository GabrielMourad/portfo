import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'nahhhh'
    
    else:
        return 'try again'

def write_to_csv(data):
    with open('database.csv', mode = 'a' ,newline = '') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter = ',',  quotechar= '"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

if __name__ == '__main__':
    app.run(debug = True, port = 8000)