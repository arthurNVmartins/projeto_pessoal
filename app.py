from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/historias')
def historias():
    return render_template('historias.html')
@app.route('/recomendacao')
def recomendacao():
    return render_template('/recomendacao.html')
if __name__=='__main__':
    app.run(debug=True)