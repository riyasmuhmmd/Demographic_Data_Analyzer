
import pandas as pd
import numpy as np

def demographic_data_analyzer():
    # Load the dataset
    df = pd.read_csv("adult.data.csv")

    # How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / len(df)) * 100, 1)

    # People with advanced education (Bachelors, Masters, Doctorate)
    advanced_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage of advanced education earners >50K
    higher_edu_rich = round((advanced_edu[advanced_edu['salary'] == '>50K'].shape[0] / len(advanced_edu)) * 100, 1)

    # People without advanced education
    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage of lower education earners >50K
    lower_edu_rich = round((lower_edu[lower_edu['salary'] == '>50K'].shape[0] / len(lower_edu)) * 100, 1)

    # Minimum hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # Percentage of people who work min hours per week and earn >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = round((min_workers[min_workers['salary'] == '>50K'].shape[0] / len(min_workers)) * 100, 1)

    # Country with highest percentage of >50K earners
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_count = df['native-country'].value_counts()
    country_rich_percentage = (country_salary / country_count * 100).dropna()
    top_country = country_rich_percentage.idxmax()
    top_country_percentage = round(country_rich_percentage.max(), 1)

    # Most popular occupation for >50K earners in India
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_occupation = india_high_earners['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_edu_rich': higher_edu_rich,
        'lower_edu_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_min_workers': rich_min_workers,
        'top_country': top_country,
        'top_country_percentage': top_country_percentage,
        'top_occupation': top_occupation
    }