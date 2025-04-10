from flask import Flask, render_template, request, redirect, url_for
from modules.job_scraper import scrape_jobs
from modules.resume_tailor_module import tailor_resume
from modules.tracker import log_application

app = Flask(__name__)
print("Function loaded!")
print(tailor_resume("Analyze machine learning models."))
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        role = request.form["role"]
        location = request.form["location"]
        jobs = scrape_jobs(role, location)
        print("DEBUG: Jobs found ->", jobs)
        return render_template("jobs.html", jobs=jobs)
    return render_template("index.html")


@app.route("/apply", methods=["POST"])
def apply():
    job_data = request.form.to_dict()
    tailored_resume = tailor_resume(job_data["description"])
    log_application(job_data, tailored_resume)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)