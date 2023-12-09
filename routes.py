import logging
import sys
from app import app
from forms import MeasurementForm
from flask import render_template, redirect, url_for

# Configure the Flask logger to write to stdout
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/measurements', methods=['GET', 'POST'])
def measurements():
    form = MeasurementForm()
    app.logger.info(f"Form submitted: {form.data}")  # Log the form data whenever the form is submitted
    if form.validate_on_submit():
        # Process form data
        form_data = form.data  # This is a dictionary of the form data
        app.logger.info(f"Form is valid: {form_data}")  # Log the form data when the form is valid

        # You can also access individual fields like this:
        # Assuming your form has fields named 'field1', 'field2', etc.
        for field in form:
            app.logger.info(f"{field.label.text}: {field.data}")

        return redirect(url_for('index'))  # Redirect to another route after submission
    else:
        app.logger.info(f"Form is not valid: {form.errors}")  # Log the form errors when the form is not valid
    return render_template('measurements.html', form=form)