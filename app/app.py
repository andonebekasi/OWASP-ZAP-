from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a vulnerable web app!"

@app.route('/vuln', methods=['GET', 'POST'])
def vuln():
    # Simulated SQL Injection vulnerability
    user_input = request.args.get('input')
    return f"User input: {user_input}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
