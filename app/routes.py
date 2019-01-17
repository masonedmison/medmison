from app import app

@app.route('/')
@app.route('/login')

def login():
	return 'hello world!'  
