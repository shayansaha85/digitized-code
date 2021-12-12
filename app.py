from flask import *
import cleaner
import generate_unique_sl

app = Flask(__name__, static_url_path="/static")

@app.route("/", methods = ["GET", "POST"])
def mainpage():
    number_of_codes = None
    cleaner.clean_folder()
    if request.method == "POST":
        number_of_codes = request.form.get("count")
        if number_of_codes is not None:
            print(int(number_of_codes))
            generate_unique_sl.codegenerator(number_of_codes)
    return render_template("index.html", number=number_of_codes)

@app.route('/download')
def download_file():
	path = f"static/downloads/serials.zip"
	return send_file(path, as_attachment=True)

if '__main__' == __name__:
    app.run()