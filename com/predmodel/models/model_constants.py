AGE_ALLOWED = [
    "75+ years",
    "55-74 years",
    "35-54 years",
    "25-34 years",
    "15-24 years",
    "5-14 years",
]

COLUMNS_ORDER = [
    'year',
    'population',
    'gdp_per_capita ($)',
    'sex_male',
    'age_midpoint',
    'gdp_for_yearM',
    'generation_Boomers',
    'generation_G.I. Generation',
    'generation_Generation X',
    'generation_Generation Z',
    'generation_Millenials',
    'generation_Silent'
]

ALL_GENERATION_COLUMNS = [
    'generation_Boomers',
    'generation_G.I. Generation',
    'generation_Generation X',
    'generation_Generation Z',
    'generation_Millenials',
    'generation_Silent',
]

COUNTRIES_ALLOWED = ["USA"]

GENERATION_BIRTH_YEARS = {
    'G.I. Generation': (1901, 1927),
    'Silent': (1928, 1945),
    'Boomers': (1946, 1964),
    'Generation X': (1965, 1980),
    'Millenials': (1981, 1996),
    'Generation Z': (1997, 2012),
}