# Import Required Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import interact, widgets

# Set seaborn style for plots
sns.set(style="whitegrid")

base_path = '~/Repos/gabrielcruzg3/college/project/'
path_CSV = f'{base_path}MICRODADOS_ED_SUP_IES_2023.CSV'



# Load and Explore Data

# Load the CSV data into pandas DataFrames
data = pd.read_csv(path_CSV, delimiter=';', encoding='latin-1')

# Display the first few rows of the DataFrame to understand its structure
data.head()

# Display basic information about the DataFrame
data.info()

# Display summary statistics of the DataFrame
data.describe()

# Check for missing values in the DataFrame
missing_values = data.isnull().sum()
missing_values[missing_values > 0]

# Display the unique values in the 'TP_ORGANIZACAO_ACADEMICA' column
data['TP_ORGANIZACAO_ACADEMICA'].unique()

# Display the unique values in the 'TP_CATEGORIA_ADMINISTRATIVA' column
data['TP_CATEGORIA_ADMINISTRATIVA'].unique()

# Plot the distribution of 'TP_ORGANIZACAO_ACADEMICA'
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='TP_ORGANIZACAO_ACADEMICA')
plt.title('Distribution of Academic Organization Types')
plt.xlabel('Academic Organization Type')
plt.ylabel('Count')
plt.show()

# Plot the distribution of 'TP_CATEGORIA_ADMINISTRATIVA'
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='TP_CATEGORIA_ADMINISTRATIVA')
plt.title('Distribution of Administrative Category Types')
plt.xlabel('Administrative Category Type')
plt.ylabel('Count')
plt.show()





# Analyze the number and types of institutions (public or private) and their academic classifications

# Group data by 'TP_CATEGORIA_ADMINISTRATIVA' and count the number of institutions
institutions_by_category = data.groupby('TP_CATEGORIA_ADMINISTRATIVA').size().reset_index(name='Count')

# Display the grouped data
institutions_by_category

# Plot the number of institutions by administrative category
plt.figure(figsize=(10, 6))
sns.barplot(data=institutions_by_category, x='TP_CATEGORIA_ADMINISTRATIVA', y='Count')
plt.title('Number of Institutions by Administrative Category')
plt.xlabel('Administrative Category Type')
plt.ylabel('Number of Institutions')
plt.show()

# Group data by 'TP_ORGANIZACAO_ACADEMICA' and count the number of institutions
institutions_by_organization = data.groupby('TP_ORGANIZACAO_ACADEMICA').size().reset_index(name='Count')

# Display the grouped data
institutions_by_organization

# Plot the number of institutions by academic organization type
plt.figure(figsize=(10, 6))
sns.barplot(data=institutions_by_organization, x='TP_ORGANIZACAO_ACADEMICA', y='Count')
plt.title('Number of Institutions by Academic Organization Type')
plt.xlabel('Academic Organization Type')
plt.ylabel('Number of Institutions')
plt.show()

# Combine both groupings into a single DataFrame for comparison
combined_data = data.groupby(['TP_CATEGORIA_ADMINISTRATIVA', 'TP_ORGANIZACAO_ACADEMICA']).size().reset_index(name='Count')

# Display the combined data
combined_data

# Plot the combined data to compare the number of institutions by both categories
plt.figure(figsize=(14, 8))
sns.barplot(data=combined_data, x='TP_CATEGORIA_ADMINISTRATIVA', y='Count', hue='TP_ORGANIZACAO_ACADEMICA')
plt.title('Number of Institutions by Administrative Category and Academic Organization Type')
plt.xlabel('Administrative Category Type')
plt.ylabel('Number of Institutions')
plt.legend(title='Academic Organization Type')
plt.show()








# Cursos de Graduação

# Extract relevant columns for course analysis
course_data = data[['NO_IES', 'TP_ORGANIZACAO_ACADEMICA', 'TP_CATEGORIA_ADMINISTRATIVA', 'QT_TEC_TOTAL', 'QT_DOC_TOTAL']]

# Display the first few rows of the course data
course_data.head()

# Analyze the distribution of teaching modalities (in-person or distance)
# Assuming 'TP_MODALIDADE_ENSINO' column exists for teaching modalities
if 'TP_MODALIDADE_ENSINO' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='TP_MODALIDADE_ENSINO')
    plt.title('Distribution of Teaching Modalities')
    plt.xlabel('Teaching Modality')
    plt.ylabel('Count')
    plt.show()

# Analyze the distribution of academic degrees (bachelor's, licentiate, or technological)
# Assuming 'TP_GRAU_ACADEMICO' column exists for academic degrees
if 'TP_GRAU_ACADEMICO' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='TP_GRAU_ACADEMICO')
    plt.title('Distribution of Academic Degrees')
    plt.xlabel('Academic Degree')
    plt.ylabel('Count')
    plt.show()

# Analyze the distribution of areas of knowledge
# Assuming 'TP_AREA_CONHECIMENTO' column exists for areas of knowledge
if 'TP_AREA_CONHECIMENTO' in data.columns:
    plt.figure(figsize=(12, 8))
    sns.countplot(data=data, y='TP_AREA_CONHECIMENTO', order=data['TP_AREA_CONHECIMENTO'].value_counts().index)
    plt.title('Distribution of Areas of Knowledge')
    plt.xlabel('Count')
    plt.ylabel('Area of Knowledge')
    plt.show()

# Group data by 'TP_MODALIDADE_ENSINO' and count the number of courses
if 'TP_MODALIDADE_ENSINO' in data.columns:
    courses_by_modality = data.groupby('TP_MODALIDADE_ENSINO').size().reset_index(name='Count')
    courses_by_modality

# Group data by 'TP_GRAU_ACADEMICO' and count the number of courses
if 'TP_GRAU_ACADEMICO' in data.columns:
    courses_by_degree = data.groupby('TP_GRAU_ACADEMICO').size().reset_index(name='Count')
    courses_by_degree

# Group data by 'TP_AREA_CONHECIMENTO' and count the number of courses
if 'TP_AREA_CONHECIMENTO' in data.columns:
    courses_by_area = data.groupby('TP_AREA_CONHECIMENTO').size().reset_index(name='Count')
    courses_by_area

# Plot the number of courses by teaching modality
if 'TP_MODALIDADE_ENSINO' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(data=courses_by_modality, x='TP_MODALIDADE_ENSINO', y='Count')
    plt.title('Number of Courses by Teaching Modality')
    plt.xlabel('Teaching Modality')
    plt.ylabel('Number of Courses')
    plt.show()

# Plot the number of courses by academic degree
if 'TP_GRAU_ACADEMICO' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(data=courses_by_degree, x='TP_GRAU_ACADEMICO', y='Count')
    plt.title('Number of Courses by Academic Degree')
    plt.xlabel('Academic Degree')
    plt.ylabel('Number of Courses')
    plt.show()

# Plot the number of courses by area of knowledge
if 'TP_AREA_CONHECIMENTO' in data.columns:
    plt.figure(figsize=(12, 8))
    sns.barplot(data=courses_by_area, y='TP_AREA_CONHECIMENTO', x='Count')
    plt.title('Number of Courses by Area of Knowledge')
    plt.xlabel('Number of Courses')
    plt.ylabel('Area of Knowledge')
    plt.show()
    
data.head()





# Vagas, Matrículas e Concluintes

# Check available columns
print(data.columns)

# Extract relevant columns for analysis
# Assuming 'QT_DOC_TOTAL' and 'QT_TEC_TOTAL' are available columns
vacancies_data = data[['NO_IES', 'QT_DOC_TOTAL', 'QT_TEC_TOTAL']]

# Display the first few rows of the vacancies data
vacancies_data.head()

# Check for missing values in the vacancies data
missing_values_vacancies = vacancies_data.isnull().sum()
missing_values_vacancies[missing_values_vacancies > 0]

# Fill missing values with 0 (assuming missing values indicate no data available)
vacancies_data.fillna(0, inplace=True)

# Group data by institution and sum the columns
vacancies_by_institution = vacancies_data.groupby('NO_IES').sum().reset_index()

# Display the grouped data
vacancies_by_institution.head()

# Plot the total number of documents by institution
plt.figure(figsize=(14, 8))
sns.barplot(data=vacancies_by_institution, x='QT_DOC_TOTAL', y='NO_IES', order=vacancies_by_institution.sort_values('QT_DOC_TOTAL', ascending=False)['NO_IES'])
plt.title('Total Number of Documents by Institution')
plt.xlabel('Total Number of Documents')
plt.ylabel('Institution')
plt.show()

# Plot the total number of technicians by institution
plt.figure(figsize=(14, 8))
sns.barplot(data=vacancies_by_institution, x='QT_TEC_TOTAL', y='NO_IES', order=vacancies_by_institution.sort_values('QT_TEC_TOTAL', ascending=False)['NO_IES'])
plt.title('Total Number of Technicians by Institution')
plt.xlabel('Total Number of Technicians')
plt.ylabel('Institution')
plt.show()




# Perfil dos Discentes e Docentes

# Analyze the age group distribution of students
age_columns = ['QT_DOC_EX_0_29', 'QT_DOC_EX_30_34', 'QT_DOC_EX_35_39', 'QT_DOC_EX_40_44', 'QT_DOC_EX_45_49', 'QT_DOC_EX_50_54', 'QT_DOC_EX_55_59', 'QT_DOC_EX_60_MAIS']
age_data = data[age_columns].sum().reset_index()
age_data.columns = ['Age Group', 'Count']

# Plot the age group distribution of students
plt.figure(figsize=(12, 8))
sns.barplot(data=age_data, x='Age Group', y='Count')
plt.title('Age Group Distribution of Students')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()

# Analyze the distribution of teaching modalities among students
if 'TP_MODALIDADE_ENSINO' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='TP_MODALIDADE_ENSINO')
    plt.title('Distribution of Teaching Modalities Among Students')
    plt.xlabel('Teaching Modality')
    plt.ylabel('Count')
    plt.show()

# Analyze the geographic distribution of students
if 'NO_UF_IES' in data.columns:
    plt.figure(figsize=(14, 8))
    sns.countplot(data=data, y='NO_UF_IES', order=data['NO_UF_IES'].value_counts().index)
    plt.title('Geographic Distribution of Students by State')
    plt.xlabel('Count')
    plt.ylabel('State')
    plt.show()

# Analyze the qualification of professors
qualification_columns = ['QT_DOC_EX_ESP', 'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT']
qualification_data = data[qualification_columns].sum().reset_index()
qualification_data.columns = ['Qualification', 'Count']

# Plot the qualification of professors
plt.figure(figsize=(10, 6))
sns.barplot(data=qualification_data, x='Qualification', y='Count')
plt.title('Qualification of Professors')
plt.xlabel('Qualification')
plt.ylabel('Count')
plt.show()

# Analyze the work regime of professors
if 'TP_REGIME_TRABALHO' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='TP_REGIME_TRABALHO')
    plt.title('Work Regime of Professors')
    plt.xlabel('Work Regime')
    plt.ylabel('Count')
    plt.show()

# Analyze the institutional affiliation of professors
if 'TP_VINCULO_INSTITUCIONAL' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='TP_VINCULO_INSTITUCIONAL')
    plt.title('Institutional Affiliation of Professors')
    plt.xlabel('Institutional Affiliation')
    plt.ylabel('Count')
    plt.show()
    
    
    
    
# Develop Vocational Affinity Questionnaire

# Define a function to create the vocational affinity questionnaire
def create_questionnaire():
    questions = [
        "1. Do you prefer working with numbers and data? (Yes/No)",
        "2. Are you interested in understanding how things work? (Yes/No)",
        "3. Do you enjoy helping others and working in teams? (Yes/No)",
        "4. Are you interested in creative activities like art or music? (Yes/No)",
        "5. Do you prefer working outdoors or with nature? (Yes/No)",
        "6. Are you interested in technology and computers? (Yes/No)",
        "7. Do you enjoy solving complex problems? (Yes/No)",
        "8. Are you interested in business and management? (Yes/No)",
        "9. Do you prefer hands-on activities and working with tools? (Yes/No)",
        "10. Are you interested in social sciences and humanities? (Yes/No)"
    ]
    return questions

# Display the questionnaire
questionnaire = create_questionnaire()
for question in questionnaire:
    print(question)

# Define a function to correlate responses to areas of undergraduate courses
def correlate_responses(responses):
    # Example correlation logic (this should be replaced with actual correlation logic)
    areas_of_interest = {
        "Yes": ["Engineering", "Computer Science", "Business"],
        "No": ["Arts", "Humanities", "Social Sciences"]
    }
    correlated_areas = []
    for response in responses:
        if response == "Yes":
            correlated_areas.extend(areas_of_interest["Yes"])
        else:
            correlated_areas.extend(areas_of_interest["No"])
    return correlated_areas

# Example responses from a student
student_responses = ["Yes", "No", "Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"]

# Correlate the student's responses to areas of undergraduate courses
correlated_areas = correlate_responses(student_responses)
print("Based on your responses, you may be interested in the following areas of undergraduate courses:")
for area in set(correlated_areas):
    print(area)
    
    


# Create Interactive Data Visualization System

# Function to create an interactive bar plot for the number of institutions by administrative category
def plot_institutions_by_category():
    fig = px.bar(institutions_by_category, x='TP_CATEGORIA_ADMINISTRATIVA', y='Count', 
                 title='Number of Institutions by Administrative Category',
                 labels={'TP_CATEGORIA_ADMINISTRATIVA': 'Administrative Category Type', 'Count': 'Number of Institutions'})
    fig.show()

# Function to create an interactive bar plot for the number of institutions by academic organization type
def plot_institutions_by_organization():
    fig = px.bar(institutions_by_organization, x='TP_ORGANIZACAO_ACADEMICA', y='Count', 
                 title='Number of Institutions by Academic Organization Type',
                 labels={'TP_ORGANIZACAO_ACADEMICA': 'Academic Organization Type', 'Count': 'Number of Institutions'})
    fig.show()

# Function to create an interactive bar plot for the number of courses by teaching modality
def plot_courses_by_modality():
    if 'TP_MODALIDADE_ENSINO' in data.columns:
        fig = px.bar(courses_by_modality, x='TP_MODALIDADE_ENSINO', y='Count', 
                     title='Number of Courses by Teaching Modality',
                     labels={'TP_MODALIDADE_ENSINO': 'Teaching Modality', 'Count': 'Number of Courses'})
        fig.show()

# Function to create an interactive bar plot for the number of courses by academic degree
def plot_courses_by_degree():
    if 'TP_GRAU_ACADEMICO' in data.columns:
        fig = px.bar(courses_by_degree, x='TP_GRAU_ACADEMICO', y='Count', 
                     title='Number of Courses by Academic Degree',
                     labels={'TP_GRAU_ACADEMICO': 'Academic Degree', 'Count': 'Number of Courses'})
        fig.show()

# Function to create an interactive bar plot for the number of courses by area of knowledge
def plot_courses_by_area():
    if 'TP_AREA_CONHECIMENTO' in data.columns:
        fig = px.bar(courses_by_area, y='TP_AREA_CONHECIMENTO', x='Count', 
                     title='Number of Courses by Area of Knowledge',
                     labels={'TP_AREA_CONHECIMENTO': 'Area of Knowledge', 'Count': 'Number of Courses'})
        fig.show()

# Function to create an interactive bar plot for the total number of vacancies by institution
def plot_vacancies_by_institution():
    fig = px.bar(vacancies_by_institution, x='QT_VAGAS_TOTAL', y='NO_IES', 
                 title='Total Number of Vacancies by Institution',
                 labels={'QT_VAGAS_TOTAL': 'Total Number of Vacancies', 'NO_IES': 'Institution'},
                 orientation='h')
    fig.show()

# Function to create an interactive bar plot for the total number of enrollments by institution
def plot_enrollments_by_institution():
    fig = px.bar(vacancies_by_institution, x='QT_MATRICULAS_TOTAL', y='NO_IES', 
                 title='Total Number of Enrollments by Institution',
                 labels={'QT_MATRICULAS_TOTAL': 'Total Number of Enrollments', 'NO_IES': 'Institution'},
                 orientation='h')
    fig.show()

# Function to create an interactive bar plot for the total number of graduates by institution
def plot_graduates_by_institution():
    fig = px.bar(vacancies_by_institution, x='QT_CONCLUINTES_TOTAL', y='NO_IES', 
                 title='Total Number of Graduates by Institution',
                 labels={'QT_CONCLUINTES_TOTAL': 'Total Number of Graduates', 'NO_IES': 'Institution'},
                 orientation='h')
    fig.show()

# Function to create an interactive bar plot for the total number of vacancies by course
def plot_vacancies_by_course():
    fig = px.bar(vacancies_by_course, x='QT_VAGAS_TOTAL', y='NO_CURSO', 
                 title='Total Number of Vacancies by Course',
                 labels={'QT_VAGAS_TOTAL': 'Total Number of Vacancies', 'NO_CURSO': 'Course'},
                 orientation='h')
    fig.show()

# Function to create an interactive bar plot for the total number of enrollments by course
def plot_enrollments_by_course():
    fig = px.bar(vacancies_by_course, x='QT_MATRICULAS_TOTAL', y='NO_CURSO', 
                 title='Total Number of Enrollments by Course',
                 labels={'QT_MATRICULAS_TOTAL': 'Total Number of Enrollments', 'NO_CURSO': 'Course'},
                 orientation='h')
    fig.show()

# Function to create an interactive bar plot for the total number of graduates by course
def plot_graduates_by_course():
    fig = px.bar(vacancies_by_course, x='QT_CONCLUINTES_TOTAL', y='NO_CURSO', 
                 title='Total Number of Graduates by Course',
                 labels={'QT_CONCLUINTES_TOTAL': 'Total Number of Graduates', 'NO_CURSO': 'Course'},
                 orientation='h')
    fig.show()

# Interactive widgets to select and display the plots
interact(plot_institutions_by_category)
interact(plot_institutions_by_organization)
interact(plot_courses_by_modality)
interact(plot_courses_by_degree)
interact(plot_courses_by_area)
interact(plot_vacancies_by_institution)
interact(plot_enrollments_by_institution)
interact(plot_graduates_by_institution)
interact(plot_vacancies_by_course)
interact(plot_enrollments_by_course)
interact(plot_graduates_by_course)
    
    
    
    
    
    
    
    
    
    # Analyze Educational Trends

# Analyze trends in the number of institutions over the years
institutions_over_years = data.groupby('NU_ANO_CENSO').size().reset_index(name='Count')

# Plot the number of institutions over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=institutions_over_years, x='NU_ANO_CENSO', y='Count', marker='o')
plt.title('Number of Institutions Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Institutions')
plt.show()

# Analyze trends in the number of courses offered over the years
if 'NU_ANO_CENSO' in data.columns and 'NO_CURSO' in data.columns:
    courses_over_years = data.groupby('NU_ANO_CENSO')['NO_CURSO'].nunique().reset_index(name='Count')

    # Plot the number of courses offered over the years
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=courses_over_years, x='NU_ANO_CENSO', y='Count', marker='o')
    plt.title('Number of Courses Offered Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Courses')
    plt.show()

# Analyze trends in the number of enrollments over the years
if 'NU_ANO_CENSO' in data.columns and 'QT_MATRICULAS_TOTAL' in data.columns:
    enrollments_over_years = data.groupby('NU_ANO_CENSO')['QT_MATRICULAS_TOTAL'].sum().reset_index(name='Total Enrollments')

    # Plot the number of enrollments over the years
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=enrollments_over_years, x='NU_ANO_CENSO', y='Total Enrollments', marker='o')
    plt.title('Number of Enrollments Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Total Enrollments')
    plt.show()

# Analyze trends in the number of graduates over the years
if 'NU_ANO_CENSO' in data.columns and 'QT_CONCLUINTES_TOTAL' in data.columns:
    graduates_over_years = data.groupby('NU_ANO_CENSO')['QT_CONCLUINTES_TOTAL'].sum().reset_index(name='Total Graduates')

    # Plot the number of graduates over the years
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=graduates_over_years, x='NU_ANO_CENSO', y='Total Graduates', marker='o')
    plt.title('Number of Graduates Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Total Graduates')
    plt.show()

# Analyze trends in the number of vacancies over the years
if 'NU_ANO_CENSO' in data.columns and 'QT_VAGAS_TOTAL' in data.columns:
    vacancies_over_years = data.groupby('NU_ANO_CENSO')['QT_VAGAS_TOTAL'].sum().reset_index(name='Total Vacancies')

    # Plot the number of vacancies over the years
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=vacancies_over_years, x='NU_ANO_CENSO', y='Total Vacancies', marker='o')
    plt.title('Number of Vacancies Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Total Vacancies')
    plt.show()

# Analyze trends in the number of institutions by region over the years
if 'NU_ANO_CENSO' in data.columns and 'NO_REGIAO_IES' in data.columns:
    institutions_by_region = data.groupby(['NU_ANO_CENSO', 'NO_REGIAO_IES']).size().reset_index(name='Count')

    # Plot the number of institutions by region over the years
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=institutions_by_region, x='NU_ANO_CENSO', y='Count', hue='NO_REGIAO_IES', marker='o')
    plt.title('Number of Institutions by Region Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Institutions')
    plt.legend(title='Region')
    plt.show()

# Analyze trends in the number of courses by region over the years
if 'NU_ANO_CENSO' in data.columns and 'NO_REGIAO_IES' in data.columns and 'NO_CURSO' in data.columns:
    courses_by_region = data.groupby(['NU_ANO_CENSO', 'NO_REGIAO_IES'])['NO_CURSO'].nunique().reset_index(name='Count')

    # Plot the number of courses by region over the years
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=courses_by_region, x='NU_ANO_CENSO', y='Count', hue='NO_REGIAO_IES', marker='o')
    plt.title('Number of Courses by Region Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Courses')
    plt.legend(title='Region')
    plt.show()

# Analyze trends in the number of enrollments by region over the years
if 'NU_ANO_CENSO' in data.columns and 'NO_REGIAO_IES' in data.columns and 'QT_MATRICULAS_TOTAL' in data.columns:
    enrollments_by_region = data.groupby(['NU_ANO_CENSO', 'NO_REGIAO_IES'])['QT_MATRICULAS_TOTAL'].sum().reset_index(name='Total Enrollments')

    # Plot the number of enrollments by region over the years
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=enrollments_by_region, x='NU_ANO_CENSO', y='Total Enrollments', hue='NO_REGIAO_IES', marker='o')
    plt.title('Number of Enrollments by Region Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Total Enrollments')
    plt.legend(title='Region')
    plt.show()

# Analyze trends in the number of graduates by region over the years
if 'NU_ANO_CENSO' in data.columns and 'NO_REGIAO_IES' in data.columns and 'QT_CONCLUINTES_TOTAL' in data.columns:
    graduates_by_region = data.groupby(['NU_ANO_CENSO', 'NO_REGIAO_IES'])['QT_CONCLUINTES_TOTAL'].sum().reset_index(name='Total Graduates')

    # Plot the number of graduates by region over the years
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=graduates_by_region, x='NU_ANO_CENSO', y='Total Graduates', hue='NO_REGIAO_IES', marker='o')
    plt.title('Number of Graduates by Region Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Total Graduates')
    plt.legend(title='Region')
    plt.show()

# Analyze trends in the number of vacancies by region over the years
if 'NU_ANO_CENSO' in data.columns and 'NO_REGIAO_IES' in data.columns and 'QT_VAGAS_TOTAL' in data.columns:
    vacancies_by_region = data.groupby(['NU_ANO_CENSO', 'NO_REGIAO_IES'])['QT_VAGAS_TOTAL'].sum().reset_index(name='Total Vacancies')

    # Plot the number of vacancies by region over the years
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=vacancies_by_region, x='NU_ANO_CENSO', y='Total Vacancies', hue='NO_REGIAO_IES', marker='o')
    plt.title('Number of Vacancies by Region Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Total Vacancies')
    plt.legend(title='Region')
    plt.show()