from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fr.html')

@app.route('/execute-python')
def execute_python():
    # Replace 'your_script.py' with the name of your Python file
    result = subprocess.run(['python', 'facial.py'], capture_output=True)
    return result.stdout.decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)
