
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate random datetime between two datetime objects
def random_datetime(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# General specs
num_rows = 5000
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)

# Encounter Fields
facilities = ['H001', 'H002', 'H003']
urns = [f'P{str(i).zfill(4)}' for i in range(1, num_rows + 1)]
admitted = 1

# Generate data
data = []
for urn in urns:
    fac_id = random.choice(facilities)
    arr_datetime = random_datetime(start_date, end_date)
    adm_datetime = arr_datetime + timedelta(hours=random.randint(1, 24))
    dis_datetime = adm_datetime + timedelta(days=random.uniform(1, 30))
    los = round((dis_datetime - adm_datetime).total_seconds() / 86400, 2)
    expired = 1 if random.random() < 0.05 else 0

    screen_flag = 1 if random.random() < 0.5 else 0
    screen_datetime = random_datetime(arr_datetime, adm_datetime) if screen_flag else None

    order_set_flag = 1 if random.random() < 0.5 else 0
    order_set_datetime = random_datetime(adm_datetime, dis_datetime) if order_set_flag else None

    cam_datetime = random_datetime(adm_datetime, dis_datetime)
    screen_to_cam_in_hr = round((cam_datetime - screen_datetime).total_seconds() / 3600, 2) if screen_datetime else 0
    cam_to_order_set_in_hr = round((order_set_datetime - cam_datetime).total_seconds() / 3600, 2) if order_set_datetime else None

    date_time_suspected = random_datetime(cam_datetime, dis_datetime) if random.random() < 0.5 else None
    avg_delirium_days_in_hr = round(random.uniform(0, 72), 2) if date_time_suspected else 0

    risk_of_delirium = 1
    confirmed_delirium = 1 if date_time_suspected else 0

    contributing_medication = random.choice([f'Medication {i}' for i in range(1, 11)] + [None])
    contributing_medication_datetime = random_datetime(arr_datetime, dis_datetime) if contributing_medication else None

    age_group = random.choice(['35-44', '45-54', '55-64', '65-74', '75-84', '85-94', '95+'])

    data.append([
        fac_id, urn, arr_datetime, adm_datetime, dis_datetime, admitted, los, expired,
        screen_datetime, screen_flag, order_set_datetime, order_set_flag,
        cam_datetime, date_time_suspected, avg_delirium_days_in_hr,
        screen_to_cam_in_hr, cam_to_order_set_in_hr,
        risk_of_delirium, confirmed_delirium, contributing_medication, contributing_medication_datetime,
        age_group
    ])

# Create DataFrame
columns = [
    'FacID', 'URN', 'ArrDateTime', 'AdmDateTime', 'DisDateTime', 'Admitted', 'LOS', 'Expired',
    'ScreenDateTime', 'ScreenFlag', 'OrderSetDateTime', 'OrderSetFlag',
    'CAMDateTime', 'DateTimeSuspected', 'AvgDeliriumDaysInHr',
    'ScreenToCAMInHour', 'CAMToOrderSetInHour',
    'RiskOfDelirium', 'ConfirmedDelirium', 'ContributingMedication', 'ContributingMedicationDateTime',
    'AgeGroup'
]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('synthetic_dataset.csv', index=False)
