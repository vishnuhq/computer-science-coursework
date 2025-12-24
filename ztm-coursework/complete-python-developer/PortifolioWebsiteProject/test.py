from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_txtfile(data):
    user_email = data["email"]
    user_subject = data["subject"]
    user_message = data["message"]
    with open("database.txt", "a") as my_database:
        my_database.write(f"\n{user_email},{user_subject},{user_message}")


def write_to_csv(data):
    user_email = data["email"]
    user_subject = data["subject"]
    user_message = data["message"]
    with open("database.csv", newline="", mode="a") as database:
        writer = csv.writer(database)
        writer.writerow([user_email, user_subject, user_message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_txtfile(data)
            write_to_csv(data)
        except:
            return "Did not save to database"
    else:
        return "Something went wrong"
    return redirect("thankyou.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
