from app import app
from forms import MeasurementForm
from flask import render_template, redirect, url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/measurements', methods=['GET', 'POST'])
def measurements():
    form = MeasurementForm()
    if form.validate_on_submit():
        # Process form data
        form_data = form.data  # This is a dictionary of the form data
        print(form_data)  # Print the form data to the console for debugging

        # You can also access individual fields like this:
        # Assuming your form has fields named 'field1', 'field2', etc.
        for field in form:
            print(f"{field.label.text}: {field.data}")

        return redirect(url_for('index'))  # Redirect to another route after submission
    return render_template('measurements.html', form=form)