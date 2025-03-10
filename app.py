from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Redirection vers une page HTML d'accueil

@app.route('/projet', methods=['GET', 'POST'])
def projet():
    result = ""
    if request.method == 'POST':
        try:
            # Récupération des valeurs depuis le formulaire
            x_A = float(request.form['x_A'])
            D_AB_exp = float(request.form['D_AB_exp'])
            r_A = float(request.form['r_A'])
            q_A = float(request.form['q_A'])
            r_B = float(request.form['r_B'])
            q_B = float(request.form['q_B'])
            lambda_A = float(request.form['lambda_A'])
            lambda_B = float(request.form['lambda_B'])
            a_AB = float(request.form['a_AB'])
            a_BA = float(request.form['a_BA'])
            tau_AB = float(request.form['tau_AB'])
            tau_BA = float(request.form['tau_BA'])
            phi_A = float(request.form['phi_A'])
            phi_B = float(request.form['phi_B'])
            theta_A = float(request.form['theta_A'])
            theta_B = float(request.form['theta_B'])
            theta_AB = float(request.form['theta_AB'])
            theta_AA = float(request.form['theta_AA'])
            theta_BB = float(request.form['theta_BB'])
            theta_BA = float(request.form['theta_BA'])
            D_AB_pur = float(request.form['D_AB_pur'])
            D_BA_pur = float(request.form['D_BA_pur'])

            # Calculs
            x_B = 1 - x_A  
            A = x_B * np.log(D_AB_pur) + (x_A * np.log(D_BA_pur))
            B = x_A * x_B
            C = (phi_A / x_A) * (1 - (lambda_A / lambda_B))
            D = (phi_B / x_B) * (1 - (lambda_B / lambda_A))
            E = x_B * q_A
            H = x_A * q_B
            F = (1 - theta_BA**2) * np.log(tau_BA)
            G = (1 - theta_BB**2) * tau_AB * np.log(tau_AB)
            I = (1 - theta_AB**2) * np.log(tau_AB)
            J = (1 - theta_AA**2) * tau_BA * np.log(tau_BA)
            K = x_A * np.log(x_A / phi_A)
            L = x_B * np.log(x_B / phi_B)
            
            ln_D_AB = A + (2 * B * (C + D)) + E * (F + G) + H * (I + J) + (2 * (K + L))
            D_AB = np.exp(ln_D_AB)
            error = (D_AB_exp - D_AB) / D_AB_exp * 100

            result = f"Coefficient de diffusion: {D_AB:.5e} cm²/s<br>Erreur relative: {error:.1f}%"
        except ValueError:
            result = "Erreur : Veuillez entrer des valeurs numériques valides."

    return render_template('projet.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
