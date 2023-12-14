def calculate_foundation(measurements):
    # calculations for Foundation
    mudsill = measurements['foundation_lf'] * 1.05
    sillSeal = measurements['foundation_lf'] / 50
    return {'Mudsill': mudsill, 'Sill Seal': sillSeal}

# def calculate_floors(measurements):
#     # calculations for Floors
#     item1 = formula1(measurements)
#     item2 = formula2(measurements)
#     # ...
#     return {'item1': item1, 'item2': item2, ...}

# def calculate_decking(measurements):
#     # calculations for Decking
#     item1 = formula1(measurements)
#     item2 = formula2(measurements)
#     # ...
#     return {'item1': item1, 'item2': item2, ...}

# def calculate_walls(measurements):
#     # calculations for Walls
#     item1 = formula1(measurements)
#     item2 = formula2(measurements)
#     # ...
#     return {'item1': item1, 'item2': item2, ...}

# def calculate_roof(measurements):
#     # calculations for Roof
#     item1 = formula1(measurements)
#     item2 = formula2(measurements)
#     # ...
#     return {'item1': item1, 'item2': item2, ...}

# def calculate_insulation(measurements):
#     # calculations for Insulation
#     item1 = formula1(measurements)
#     item2 = formula2(measurements)
#     # ...
#     return {'item1': item1, 'item2': item2, ...}

# def calculate_drywall(measurements):
#     # calculations for Drywall
#     item1 = formula1(measurements)
#     item2 = formula2(measurements)
#     # ...
#     return {'item1': item1, 'item2': item2, ...}

# def calculate_trim(measurements):
#     # calculations for Trim
#     item1 = formula1(measurements)
#     item2 = formula2(measurements)
#     # ...
#     return {'item1': item1, 'item2': item2, ...}

# def calculate_paint(measurements):
#     # calculations for Paint
#     item1 = formula1(measurements)
#     item2 = formula2(measurements)
#     # ...
#     return {'item1': item1, 'item2': item2, ...}

# def calculate_floor_coverings(measurements):
#     # calculations for Floor Coverings
#     item1 = formula1(measurements)
#     item2 = formula2(measurements)
#     # ...
#     return {'item1': item1, 'item2': item2, ...}

def calculate_all_categories(measurements_list):
    categories = {}
    costs = {}
    for measurements in measurements_list:
        measurements_dict = {
            'footings_lf': measurements.footings_lf,
            'foundation_lf': measurements.foundation_lf,
            'garage_sf': measurements.garage_sf,
            'basement_sf': measurements.basement_sf,
            'living_area_sf': measurements.living_area_sf,
            'garage_wall_lf': measurements.garage_wall_lf,
            'outside_wall_lf': measurements.outside_wall_lf,
            'common_wall_lf': measurements.common_wall_lf,
            'plumbing_wall_lf': measurements.plumbing_wall_lf,
            'interior_wall_lf': measurements.interior_wall_lf,
            'outside_wall_sf': measurements.outside_wall_sf,
            'gable_sf': measurements.gable_sf,
            'roof_perimeter_lf': measurements.roof_perimeter_lf,
            'roof_sf': measurements.roof_sf,
        }
        foundation = calculate_foundation(measurements_dict)
        # floors = calculate_floors(measurements_dict)
        # decking = calculate_decking(measurements_dict)
        # walls = calculate_walls(measurements_dict)
        # roof = calculate_roof(measurements_dict)
        # insulation = calculate_insulation(measurements_dict)
        # drywall = calculate_drywall(measurements_dict)
        # trim = calculate_trim(measurements_dict)
        # paint = calculate_paint(measurements_dict)
        # floor_coverings = calculate_floor_coverings(measurements_dict)

        # Add prices for each item
        prices = {
            'Mudsill': 10.0,  # price for item1
            'Sill Seal': 20.0,  # price for item2
            # add prices for other items
        }

        # Calculate cost for each item
        foundation_cost = sum(quantity * prices[item] for item, quantity in foundation.items())     
        # other categories...

        categories = {
            'Foundation': foundation,
            # 'Floors': floors,
            # 'Decking': decking,
            # 'Walls': walls,
            # 'Roof': roof,
            # 'Insulation': insulation,
            # 'Drywall': drywall,
            # 'Trim': trim,
            # 'Paint': paint,
            # 'Floor Coverings': floor_coverings,
        }

        costs = {
            'Foundation Cost': foundation_cost,
            # 'Floors Cost': floors_cost,
            # 'Decking Cost': decking_cost,
            # 'Walls Cost': walls_cost,
            # 'Roof Cost': roof_cost,
            # 'Insulation Cost': insulation_cost,
            # 'Drywall Cost': drywall_cost,
            # 'Trim Cost': trim_cost,
            # 'Paint Cost': paint_cost,
            # 'Floor Coverings Cost': floor_coverings_cost,
        }
    
    return categories, costs