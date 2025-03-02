from flask import Flask, request, render_template

app = Flask(__name__)

def factoriel(n):
    F = 1
    for i in range(1, n + 1):
        F *= i
    return F

try:
    nombre = int(input("Entrez un nombre pour calculer son factoriel (mode console) : "))
    print(f"Le factoriel de {nombre} est : {factoriel(nombre)}")
except ValueError:
    print("Erreur : Veuillez entrer un nombre entier valide.")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            number = int(request.form["number"]) 
            result = factoriel(number) 
        except ValueError:
            result = "Entrée invalide ! Veuillez entrer un nombre entier."
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)