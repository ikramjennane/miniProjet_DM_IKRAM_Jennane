from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        variable_values = []
        for i in range(10):
            value = float(request.form[f'variable_{i+1}'])
            variable_values.append(value)

        input_data = np.array(variable_values).reshape(1, -1)

        # Remplacez la prédiction fictive par la prédiction réelle de votre modèle
        prediction = 1

        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
