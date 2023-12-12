import logging
import sys
from app import app, db
from forms import MeasurementForm, ProjectForm  # Import the ProjectForm
from models import Measurement, Project
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

        # Create a new Measurement instance
        measurement = Measurement(
            footings_lf=form.footings_lf.data,
            foundation_lf=form.foundation_lf.data,
            garage_sf=form.garage_sf.data,
            basement_sf=form.basement_sf.data,
            living_area_sf=form.living_area_sf.data,
            garage_wall_lf=form.garage_wall_lf.data,
            outside_wall_lf=form.outside_wall_lf.data,
            common_wall_lf=form.common_wall_lf.data,
            plumbing_wall_lf=form.plumbing_wall_lf.data,
            interior_wall_lf=form.interior_wall_lf.data,
            outside_wall_sf=form.outside_wall_sf.data,
            gable_sf=form.gable_sf.data,
            roof_perimeter_lf=form.roof_perimeter_lf.data,
            roof_sf=form.roof_sf.data
        )
        db.session.add(measurement)
        db.session.commit()

        return redirect(url_for('index'))  # Redirect to another route after submission
    else:
        app.logger.info(f"Form is not valid: {form.errors}")  # Log the form errors when the form is not valid
    return render_template('measurements.html', form=form)

@app.route('/projects')
def projects():
    projects = Project.query.all()  # Query the Project objects
    return render_template('projects.html', projects=projects)  # Pass the projects to the template

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('projects'))
    return render_template('add_project.html', form=form)