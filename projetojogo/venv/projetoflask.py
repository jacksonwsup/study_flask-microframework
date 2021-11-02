from flask import Flask, render_template #funcção render_template utilizamos para renderizar qualqer formato

app = Flask(__name__)
#app.run(host='0.0.0.0', port=8080)
@app.route('/inicio')

def hellow():
    return render_template('lista.html', titulo='Jogos')

app.run()