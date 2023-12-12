from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    measurements = db.relationship('Measurement', backref='project', lazy=True)

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    footings_lf = db.Column(db.Float)
    foundation_lf = db.Column(db.Float)
    garage_sf = db.Column(db.Float)
    basement_sf = db.Column(db.Float)
    living_area_sf = db.Column(db.Float)
    garage_wall_lf = db.Column(db.Float)
    outside_wall_lf = db.Column(db.Float)
    common_wall_lf = db.Column(db.Float)
    plumbing_wall_lf = db.Column(db.Float)
    interior_wall_lf = db.Column(db.Float)
    outside_wall_sf = db.Column(db.Float)
    gable_sf = db.Column(db.Float)
    roof_perimeter_lf = db.Column(db.Float)
    roof_sf = db.Column(db.Float)