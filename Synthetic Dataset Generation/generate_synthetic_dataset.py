import csv
import random
from datetime import datetime, timedelta

# Define the number of patients
num_patients = 5000

# Define the facility IDs and unit codes
fac_ids = ['H001', 'H002', 'H003']
unit_codes = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# Define the age groups
age_groups = ['35-44', '45-54', '55-64', '65-74', '75-84', '85-94', '95+']

# Define the medications
medications = [f'Medication {i}' for i in range(1, 11)]

# Define the date range
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)

# Function to generate a random datetime between two datetimes
def random_datetime(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Function to generate a synthetic patient record
def generate_patient_record(urn):
    fac_id = random.choice(fac_ids)
    arr_datetime = random_datetime(start_date, end_date)
    adm_datetime = arr_datetime + timedelta(hours=random.randint(1, 48))
    dis_datetime = adm_datetime + timedelta(days=random.uniform(1, 30))
    los = (dis_datetime - adm_datetime).total_seconds() / 86400
    expired = random.choices([0, 1], weights=[95, 5])[0]
    screen_datetime = random_datetime(arr_datetime, adm_datetime) if random.choice([True, False]) else ''
    screen_flag = 1 if screen_datetime else 0
    order_set_datetime = random_datetime(adm_datetime, dis_datetime) if random.choice([True, False]) else ''
    order_set_flag = 1 if order_set_datetime else 0
    cam_datetime = random_datetime(adm_datetime, dis_datetime)
    datetime_suspected = cam_datetime + timedelta(hours=random.uniform(0.1, 24))
    acquired_unit = f"{fac_id}-{random.choice(unit_codes)}"
    avg_delirium_days_in_hr = random.uniform(0, 72)
    screen_to_cam_in_hr = (cam_datetime - screen_datetime).total_seconds() / 3600 if screen_datetime else ''
    cam_to_order_set_in_hr = (order_set_datetime - cam_datetime).total_seconds() / 3600 if order_set_datetime else ''
    risk_of_delirium = 1
    confirmed_delirium = 1 if datetime_suspected else 0
    contributing_medication = random.choice(medications) if random.choice([True, False]) else ''
    contributing_medication_datetime = random_datetime(arr_datetime, dis_datetime) if contributing_medication else ''
    age_group = random.choice(age_groups)

    return [
        fac_id, urn, arr_datetime.strftime('%Y-%m-%d %H:%M'), adm_datetime.strftime('%Y-%m-%d %H:%M'),
        dis_datetime.strftime('%Y-%m-%d %H:%M'), 1, round(los, 2), expired, screen_datetime.strftime('%Y-%m-%d %H:%M') if screen_datetime else '',
        screen_flag, order_set_datetime.strftime('%Y-%m-%d %H:%M') if order_set_datetime else '', order_set_flag,
        round(screen_to_cam_in_hr, 2) if screen_to_cam_in_hr else '', round(cam_to_order_set_in_hr, 2) if cam_to_order_set_in_hr else '',
        cam_datetime.strftime('%Y-%m-%d %H:%M'), datetime_suspected.strftime('%Y-%m-%d %H:%M'), acquired_unit,
        round(avg_delirium_days_in_hr, 2), risk_of_delirium, confirmed_delirium, contributing_medication,
        contributing_medication_datetime.strftime('%Y-%m-%d %H:%M') if contributing_medication_datetime else '', age_group
    ]

# Generate the synthetic dataset
dataset = [generate_patient_record(f'P{str(i).zfill(4)}') for i in range(1, num_patients + 1)]

# Define the column headers
headers = [
    'FacID', 'URN', 'ArrDateTime', 'AdmDateTime', 'DisDateTime', 'Admitted', 'LOS', 'Expired', 'ScreenDateTime',
    'ScreenFlag', 'OrderSetDateTime', 'OrderSetFlag', 'ScreenToCAMInHr', 'CAMToOrderSetInHr', 'CAMDateTime',
    'DateTimeSuspected', 'AcquiredUnit', 'AvgDeliriumDaysInHr', 'RiskOfDelirium', 'ConfirmedDelirium',
    'ContributingMedication', 'ContributingMedicationDateTime', 'AgeGroup'
]

# Write the dataset to a CSV file
with open('synthetic_dataset.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(dataset)

print("Synthetic dataset has been generated and saved to 'synthetic_dataset.csv'.")
