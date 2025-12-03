def model_data_validation(data):
    from ..predmodel.models.model_constants import (
        COUNTRIES_ALLOWED, AGE_ALLOWED, GENERATION_BIRTH_YEARS
    )
    from numpy import float64, int64;

    # Checking correctness of 'country' key  
    if (not data["country"][0] in COUNTRIES_ALLOWED):
        raise ValueError("COUNTRY is NOT allowed!")
    
    # Checking correctness of 'year' key
    if (int(data["year"][0]) < 1985):
        raise ValueError("YEAR value is below 1985!")
    
    # Checking correctness of 'sex' key
    if (data["sex"][0] != "female" and data["sex"][0] != "male"):
        raise ValueError("SEX is incorrect!")
    
    # Checking correctness of 'age' key
    if (not data["age"][0] in AGE_ALLOWED):
        raise ValueError("AGE value is incorrect!")
    
    # Checking correctness of 'generation' key
    if (not data["generation"][0] in GENERATION_BIRTH_YEARS):
        raise ValueError("GENERATION is not in the list!")
    
    # Parse age range string to get min/max ages
    def parse_age_range(age_str):
        if age_str == "75+ years":
            return (75, 120)  # Max reasonable age
        age_str = age_str.replace(" years", "").strip()
        parts = age_str.split("-")
        return (int(parts[0]), int(parts[1]))
    
    min_age, max_age = parse_age_range(data["age"][0])
    
    # Calculate implied birth year range
    # A person of max_age in the given year was born in (year - max_age)
    # A person of min_age in the given year was born in (year - min_age)
    birth_year_min = int(data["year"][0]) - max_age
    birth_year_max = int(data["year"][0]) - min_age
    
    # Get generation's birth year range
    gen_birth_min, gen_birth_max = GENERATION_BIRTH_YEARS[data["generation"][0]]
    
    # Check for overlap between ranges
    # Ranges overlap if: birth_year_max >= gen_birth_min AND birth_year_min <= gen_birth_max
    has_overlap = (birth_year_max >= gen_birth_min) and (birth_year_min <= gen_birth_max)
    
    if not has_overlap:
        raise ValueError(
            f"Data mismatch: '{data["generation"][0]}' (born {gen_birth_min}-{gen_birth_max}) "
            f"is incompatible with age '{data["age"][0]}' in year {data["year"][0]}. "
            f"This would imply birth years {birth_year_min}-{birth_year_max}."
        )
    
    try:
        # Checking correctness of 'population' key
        int64(data["population"][0])

        # Checking correctness of 'gdp_for_year' key
        float64(data["gdp_for_year"][0])

        # Checking correctness of 'gdp_per_capita' key
        int64(data["gdp_per_capita"][0])
    except Exception as e:
        raise ValueError("Data convertation failed")