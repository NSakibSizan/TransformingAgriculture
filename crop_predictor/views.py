from django.shortcuts import render
import pickle
import numpy as np

def crop_prediction(request):
    if request.method == 'POST':
        # Get the input values from the form
        # Get the values from the form and validate them
        try:
            n = float(request.POST['n'])
            p = float(request.POST['p'])
            k = float(request.POST['k'])
            rain = float(request.POST['rain'])
            ph = float(request.POST['ph'])
            temp = float(request.POST['temp'])
            hum = float(request.POST['hum'])
        except ValueError:
            # Handle the case where a value is not a valid float (e.g., empty string)
            # You can redirect the user back to the form with an error message, or handle it as you see fit.
            # For example, you can set default values or return an error response.
            # Here's an example of setting default values to 0 for invalid inputs:
            n = 0
            p = 0
            k = 0
            rain = 0
            ph = 0
            temp = 0
            hum = 0

        # Load the trained model from the pickle file
        with open('DecisionTree.pkl', 'rb') as model_pkl:
            model = pickle.load(model_pkl)

        # Make the prediction
        input_data = [[n, p, k, ph, rain, temp, hum]]
        class_probabilities = model.predict_proba(input_data)

        # Get the top N predictions and their probabilities
        N = 3  # Set N to the number of top predictions you want
        top_n_classes = np.argsort(class_probabilities[0])[::-1][:N]
        predicted_crops = model.classes_[top_n_classes]
        top_n_probabilities = class_probabilities[0][top_n_classes]

        # Create a list of (crop, probability) pairs for rendering
        top_predictions = [(crop, probability) for crop, probability in zip(predicted_crops, top_n_probabilities)]

        # Render the result
        return render(request, 'index.html', {'top_predictions': top_predictions})

    return render(request, 'index.html')
