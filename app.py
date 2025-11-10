from flask import Flask, render_template, redirect

app = Flask(__name__)

# Exercício 1 — Página inicial (index)
@app.route('/')
def index():
    return '<h1>Hello, Flask !!</h1>'