from flask import Flask, render_template, redirect, url_for
from code_checker import check_code
from ticket_manager import get_tickets, create_ticket

app = Flask(__name__)

@app.route('/')
def dashboard():
    tickets = get_tickets()
    return render_template('dashboard.html', tickets=tickets)

@app.route('/scan')
def scan():
    issues = check_code('sample_code.py')
    for issue in issues:
        create_ticket(issue)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
