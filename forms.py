from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField

class MeasurementForm(FlaskForm):
    footings_lf = FloatField('Footings (linear feet)')
    foundation_lf = FloatField('Foundation (linear feet)')
    garage_sf = FloatField('Garage (square feet)')
    basement_sf = FloatField('Basement (square feet)')
    living_area_sf = FloatField('Living Area (square feet)')
    garage_wall_lf = FloatField('Garage Wall (linear feet)')
    outside_wall_lf = FloatField('Outside Wall (linear feet)')
    common_wall_lf = FloatField('Common Wall (linear feet)')
    plumbing_wall_lf = FloatField('Plumbing Wall (linear feet)')
    interior_wall_lf = FloatField('Interior Wall (linear feet)')
    outside_wall_sf = FloatField('Outside Wall (square feet)')
    gable_sf = FloatField('Gable (square feet)')
    roof_perimeter_lf = FloatField('Roof Perimeter (linear feet)')
    roof_sf = FloatField('Roof (square feet)')
    submit = SubmitField('Submit')

