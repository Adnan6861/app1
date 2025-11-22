
from flask import Flask,render_template
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
        
    }
]
@app.route('/')  
def helloAdnan():
    return render_template("index.html",jobs=JOBS,web_name="Wake Up")
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)