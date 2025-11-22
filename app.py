
from flask import Flask,render_template,jsonify
app=Flask(__name__)
JOBS=[
    {
        "id":1,
        "title":"Data Analysis",
        "job_type":"Remote",
        "salary":"Rs 1000000"
    },
        {
        "id":2,
        "title":"System Design",
        "job_type":"onsite",
        "salary":"Rs 2000000"
    },
        {
        "id":3,
        "title":"Web Developer",
        "job_type":"Hybrid",
        
    },
    {
    "id":4,
    "title":"Frontend Developer",
    "job_type":"Remote",
    "salary":"Rs 150000"
},
{
    "id":5,
    "title":"Backend Engineer",
    "job_type":"Onsite",
    "salary":"Rs 180000"
},
{
    "id":6,
    "title":"UI/UX Designer",
    "job_type":"Hybrid",
    "salary":"Rs 120000"
},
{
    "id":7,
    "title":"Mobile App Developer",
    "job_type":"Remote",
    "salary":"Rs 200000"
},
{
    "id":8,
    "title":"Machine Learning Engineer",
    "job_type":"Onsite",
    "salary":"Rs 300000"
},
{
    "id":9,
    "title":"Cloud Engineer",
    "job_type":"Hybrid",
    "salary":"Rs 250000"
},
{
    "id":10,
    "title":"IT Support Specialist",
    "job_type":"Onsite",
    "salary":"Rs 90000"
},
{
    "id":11,
    "title":"Cyber Security Analyst",
    "job_type":"Remote",
    "salary":"Rs 220000"
}

]
@app.route('/')  
def helloAdnan():
    return render_template("index.html",jobs=JOBS,web_name="Wake Up")
@app.route("/api/adnan")
def job_list():
   return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)