def data_prep(data):
    import pandas as pd
    import numpy as np
    from .models.model_constants import COLUMNS_ORDER as age_mapping
    from .models.model_constants import ALL_GENERATION_COLUMNS, COLUMNS_ORDER

    def drop_and_convert(ndata):
        ndata['population'] = ndata['population'].astype(np.int64)
        ndata['gdp_for_year'] = ndata['gdp_for_year'].astype(np.float64)
        ndata['gdp_per_capita ($)'] = ndata['gdp_per_capita'].astype(np.int64)
        ndata.drop('gdp_per_capita', axis=1, inplace=True)
    
    def sex_category_convertation(ndata):
        ndata['sex_male'] = ndata['sex'].apply(lambda x: 1 if x == "male" else 0)
        ndata.drop('sex', axis=1, inplace=True)

    def age_midpoint_calculation(ndata):
        age_mapping = {
            "75+ years": 80,
            "55-74 years": (74 + 55) / 2,
            "35-54 years": (54 + 35) / 2,
            "25-34 years": (34 + 25) / 2,
            "15-24 years": (24 + 15) / 2,
            "5-14 years": (14 + 5) / 2,
        }

        ndata['age_midpoint'] = ndata['age'].map(age_mapping)
        ndata.drop('age', axis=1, inplace=True)

    def gpd_for_year_to_millions(ndata):
        ndata['gdp_for_yearM'] = ndata['gdp_for_year'].apply(lambda x : np.float64(x / (10**6)))
        ndata.drop('gdp_for_year', axis=1, inplace=True)

    def adding_whole_generations(ndata):
        ndata = pd.concat([ndata, ndata.reindex(columns=ALL_GENERATION_COLUMNS, fill_value=0)], axis=1)
        ndata["generation_" + ndata["generation"]] = 1
        ndata.drop('generation', axis=1, inplace=True)
        return ndata

    # Убираем ненужный на данный момент параметр - страна
    ndata = data.drop(columns=["country"])
    # Конвертируем столбцы в корректные данные
    drop_and_convert(ndata)
    # Конвертируем категориальную переменную пола в логическую "мужчина?"
    sex_category_convertation(ndata)
    # Конвертируем категориальную переменную диапазона возраста в среднее для диапазона
    age_midpoint_calculation(ndata)
    # Ковертируем значение столбца в миллионы
    gpd_for_year_to_millions(ndata)
    # Добавляем все поколения в таблицу и присваиваем значение 1 для поколения запроса
    ndata = adding_whole_generations(ndata)

    # Упорядочиваем в верном порядке столбцы
    ndata = ndata[COLUMNS_ORDER]

    return ndata