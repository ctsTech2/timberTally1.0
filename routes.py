import logging
import sys
from app import app, db
from forms import MeasurementForm, ProjectForm
from models import Measurement, Project, LumberQuantity
from lumber_calculations import calculate_all_categories
from flask import render_template, redirect, url_for
from sqlalchemy.orm import joinedload

# Configure the Flask logger to write to stdout
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/measurements/<int:project_id>', methods=['GET', 'POST'])
def measurements(project_id):
    project = Project.query.get_or_404(project_id)
    form = MeasurementForm()
    if form.validate_on_submit():
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
            roof_sf=form.roof_sf.data,
            project_id=project.id
        )
        db.session.add(measurement)
        db.session.commit()

        # Calculate lumber quantities
        measurements = Measurement.query.filter_by(project_id=project.id).all()
        categories, costs = calculate_all_categories(measurements)
        for category, items in categories.items():
            for item, quantity in items.items():
                lumber_quantity = LumberQuantity(
                    category=category,
                    item=item,
                    quantity=quantity,
                    project_id=project.id
                )
                db.session.add(lumber_quantity)
        db.session.commit()

        return redirect(url_for('projects'))
    measurements = Measurement.query.filter_by(project_id=project.id).all()
    return render_template('measurements.html', form=form, project=project, measurements=measurements)

@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    measurements = Measurement.query.filter_by(project_id=project.id).all()
    categories, costs = calculate_all_categories(measurements)
    return render_template('project_detail.html', project=project, categories=categories, costs=costs)

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('measurements', project_id=project.id))
    return render_template('add_project.html', form=form)

@app.route('/delete_project/<int:id>', methods=['POST'])
def delete_project(id):
    project = Project.query.get(id)
    if project:
        measurements = Measurement.query.filter_by(project_id=id).all()
        for measurement in measurements:
            db.session.delete(measurement)
        db.session.delete(project)
        db.session.commit()
    return redirect(url_for('projects'))