from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
from cadquery import Workplane
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = float(request.form['length'])
        diameter = float(request.form['diameter'])
        pin_spacing = float(request.form['pin_spacing'])

        # Generate the 3D model of the capacitor
        model = generate_capacitor(length, diameter, pin_spacing)

        # Save the model as a STEP file and an STL file
        model.exportStep('static/capacitor.step')
        model.exportStl('static/capacitor.stl')  # Ensure it's in the static directory

        return render_template('index.html', stl_generated=True)

    return render_template('index.html', stl_generated=False)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

def generate_capacitor(length, diameter, pin_spacing):
    """
    Generate a 3D model of a capacitor based on the given parameters.
    """
    # Create the body of the capacitor
    body = (
        Workplane("XY")
        .circle(diameter / 2)
        .extrude(length)
    )

    # Create the pins
    pin_length = length / 2
    pin_diameter = diameter / 4

    # Create the first pin
    pin1 = (
        Workplane("XY")
        .circle(pin_diameter)
        .extrude(pin_length)
        .translate((pin_spacing / 2, 0, 0))
    )

    # Create the second pin
    pin2 = (
        Workplane("XY")
        .circle(pin_diameter)
        .extrude(pin_length)
        .translate((-pin_spacing / 2, 0, 0))
    )

    # Combine the body and pins
    model = body.union(pin1).union(pin2)

    return model.val()  # Return the solid

if __name__ == '__main__':
    app.run(debug=True)
