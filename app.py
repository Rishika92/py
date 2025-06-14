from flask import Flask,render_template

app = Flask(__name__)
JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'New York, USA',
        'salary':'$70,000'
    },
    {
        'id':2,
        'title':'backend Developer',
        'location':'San Francisco, USA',
        'salary':'$120,000'

    },
    {
        'id':3,
        'title':'Frontend Developer',
        'location':'London, UK',
        'salary':'$110,000'
    },
    {
        'id':4,
        'title':'Data Scientist',
        'location':'Berlin, Germany',
        'salary':'$130,000'
    },
    {
        'id':5,
        'title':'DevOps Engineer',
        'location':'Sydney, Australia',
        'salary':'$115,000'
    }
]

@app.route('/')
def hello():
    return render_template('/home.html',jobs=JOBS)

#calling api
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
