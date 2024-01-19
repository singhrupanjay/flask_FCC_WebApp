from flask import Flask
from flask import render_template
from flask import jsonify




app = Flask(__name__)

JOBS = [
  
  {
    'id' : 1,
    'title' : 'Data Scientist',
    'location' : 'Delhi, India',
    'salary' : 'Rs. 12,00,000'
  },
  {
    'id' : 2,
    'title' : 'Data Analyst',
    'location' : 'Remote',
    'salary' : 'Rs. 15,00,000'
  },
  {
    'id' : 3,
    'title' : 'Frontend Developer',
    'location' : 'San Francisco, USA'
  },
  {
    'id' : 4,
    'title' : 'Backend Developer',
    'location' : 'Mumbai, India',
    'salary' : 'Rs. 16,00,000'
  },
  
  
]

@app.route("/")
def hello():
  return render_template('home.html',
                        jobs=JOBS,company_name = 'Jovian')

@app.route("/apijobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
