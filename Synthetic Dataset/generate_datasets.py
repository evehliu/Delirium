
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate random datetime between two datetime objects
def random_datetime(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

# Generate EDMADMCombined dataset
def generate_EDMADMCombined(num_records):
    data = {
        "URN": [f"P{str(i).zfill(4)}" for i in range(1, num_records + 1)],
        "Age": np.random.randint(17, 100, num_records),
        "FacID": np.random.choice(["H001", "H002", "H003"], num_records),
        "ArrDateTime": [random_datetime(datetime(2022, 1, 1), datetime(2024, 12, 31)) for _ in range(num_records)],
        "AdmDateTime": [],
        "DisDateTime": [],
        "Admitted": [1] * num_records,
        "Expired": np.random.choice([0, 1], num_records, p=[0.95, 0.05]),
        "RiskOfDelirium": [0] * num_records,
        "ConfirmedDelirium": [0] * num_records,
        "ContributingMedication": np.random.choice([f"Medication {i}" for i in range(1, 11)] + [None], num_records),
        "ContributingMedicationDateTime": [],
        "FirstOrderSetDateTime": [],
        "OrderSetFlag": [0] * num_records,
    }

    for i in range(num_records):
        arr_dt = data["ArrDateTime"][i]
        adm_dt = random_datetime(arr_dt, arr_dt + timedelta(days=random.randint(1, 10)))
        dis_dt = random_datetime(adm_dt, adm_dt + timedelta(days=random.randint(1, 30)))
        data["AdmDateTime"].append(adm_dt)
        data["DisDateTime"].append(dis_dt)
        data["ContributingMedicationDateTime"].append(
            random_datetime(arr_dt, dis_dt) if data["ContributingMedication"][i] else None
        )
        data["FirstOrderSetDateTime"].append(
            random_datetime(arr_dt, dis_dt) if data["OrderSetFlag"][i] else None
        )

    data["LOS"] = [(dis_dt - adm_dt).days + (dis_dt - adm_dt).seconds / 86400 for adm_dt, dis_dt in zip(data["AdmDateTime"], data["DisDateTime"])]

    df_EDMADMCombined = pd.DataFrame(data)
    return df_EDMADMCombined

# Generate Delirium dataset
def generate_Delirium(df_EDMADMCombined, num_records):
    selected_urns = np.random.choice(df_EDMADMCombined["URN"], num_records, replace=False)
    data = {
        "URN": selected_urns,
        "FirstScreenDateTime": [],
        "ScreenFlag": np.random.choice([0, 1], num_records),
        "CAM": np.random.choice([0, 1, 2], num_records),
        "CAMDateTime": [],
        "ScreenToCAMInHr": [],
        "CAMToOrderSetInHr": [],
        "FirstDateTimeSuspected": [],
        "AcquiredUnit": [],
        "AvgDeliriumDaysInHr": np.random.uniform(0, 72, num_records).round(2),
    }

    for urn in selected_urns:
        patient = df_EDMADMCombined[df_EDMADMCombined["URN"] == urn].iloc[0]
        arr_dt = patient["ArrDateTime"]
        adm_dt = patient["AdmDateTime"]
        dis_dt = patient["DisDateTime"]
        screen_dt = random_datetime(arr_dt, adm_dt) if random.choice([True, False]) else None
        cam_dt = random_datetime(adm_dt, dis_dt)
        first_suspected_dt = random_datetime(cam_dt, dis_dt) if random.choice([True, False]) else None
        acquired_unit = f"{patient['FacID']}-{random.choice(['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C'])}"

        data["FirstScreenDateTime"].append(screen_dt)
        data["CAMDateTime"].append(cam_dt)
        data["ScreenToCAMInHr"].append(
            (cam_dt - screen_dt).total_seconds() / 3600 if screen_dt else None
        )
        data["CAMToOrderSetInHr"].append(
            (first_suspected_dt - cam_dt).total_seconds() / 3600 if first_suspected_dt else None
        )
        data["FirstDateTimeSuspected"].append(first_suspected_dt)
        data["AcquiredUnit"].append(acquired_unit)

    df_Delirium = pd.DataFrame(data)
    return df_Delirium

# Generate DeliriumAI dataset
def generate_DeliriumAI(df_EDMADMCombined, num_records):
    selected_urns = np.random.choice(df_EDMADMCombined["URN"], num_records, replace=False)
    data = {
        "URN": selected_urns,
        "FirstPredictedDateTime": [],
        "FirstDateTimePredictedRisk": [],
        "AcquiredUnit": [],
        "AvgDeliriumDaysInHr": np.random.uniform(0, 72, num_records).round(2),
    }

    for urn in selected_urns:
        patient = df_EDMADMCombined[df_EDMADMCombined["URN"] == urn].iloc[0]
        arr_dt = patient["ArrDateTime"]
        adm_dt = patient["AdmDateTime"]
        dis_dt = patient["DisDateTime"]
        predicted_dt = random_datetime(adm_dt, dis_dt)
        first_predicted_risk_dt = random_datetime(predicted_dt, dis_dt) if random.choice([True, False]) else None
        acquired_unit = f"{patient['FacID']}-{random.choice(['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C'])}"

        data["FirstPredictedDateTime"].append(predicted_dt)
        data["FirstDateTimePredictedRisk"].append(first_predicted_risk_dt)
        data["AcquiredUnit"].append(acquired_unit)

    df_DeliriumAI = pd.DataFrame(data)
    return df_DeliriumAI

# Generate datasets
df_EDMADMCombined = generate_EDMADMCombined(5000)
df_Delirium = generate_Delirium(df_EDMADMCombined, 2500)
df_DeliriumAI = generate_DeliriumAI(df_EDMADMCombined, 2500)

# Save datasets to CSV files
df_EDMADMCombined.to_csv("EDMADMCombined.csv", index=False)
df_Delirium.to_csv("Delirium.csv", index=False)
df_DeliriumAI.to_csv("DeliriumAI.csv", index=False)

print("Datasets generated and saved successfully.")
