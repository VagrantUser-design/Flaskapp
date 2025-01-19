from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    interest = None
    if request.method == 'POST':
        try:
            N = float(request.form['amount'])
            M = float(request.form['rate'])
            T = int(request.form['months'])
            
            # Interest calculation formula
            interest = (N * M * T) / 100
        except ValueError:
            interest = "Please enter valid numbers for all fields."

    return render_template('index.html', interest=interest)

if __name__ == '__main__':
    app.run(debug=True)
