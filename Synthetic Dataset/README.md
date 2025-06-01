
# Reusable Synthetic Dataset Generation Prompt

## Hospital Delirium Summary – First Episode per Patient

### Objective
Generate a fully synthetic dataset (no real patient data) for a Power BI dashboard focused on summarizing the first delirium episode per admitted patient, based on CAM screening events.

---

## GENERAL SPECS

- **Rows**: One row per patient (URN), up to 5,000 unique URNs
- **Patients**: Admitted only (`Admitted = 1`)
- **Time Range**: Between Jan 1, 2022 and Dec 31, 2024
- **Datetime Format**: `YYYY-MM-DD HH:MM`

---

## 1. Encounter Fields

| Column          | Description |
|-----------------|-------------|
| `FacID`         | Random hospital facility ID from `H001–H003` |
| `URN`           | Unique patient ID (e.g., `P0001–P5000`) |
| `ArrDateTime`   | Date + time the patient arrived |
| `AdmDateTime`   | Date + time admitted to inpatient unit |
| `DisDateTime`   | Date + time of discharge (must be after `AdmDateTime`) |
| `Admitted`      | Always `1` (admitted only) |
| `LOS`           | Length of stay in days (2 decimals), calculated as `DisDateTime - AdmDateTime` |
| `Expired`       | 5% chance a patient dies during visit (`1 = yes`, `0 = no`) |

---

## 2. Screening and Order Set Metadata

| Column                  | Description |
|-------------------------|-------------|
| `ScreenDateTime`        | Optional timestamp for pre-screening (must be between `ArrDateTime` and `AdmDateTime`) |
| `ScreenFlag`            | `1` if pre-screen occurred, else `0` |
| `OrderSetDateTime`      | Timestamp of earliest delirium order set placement (must be after `ScreenDateTime` if both exist) |
| `OrderSetFlag`          | `1` if order set occurred, else `0` |
| `ScreenToCAMInHr`       | Duration in hours (2 decimals) from `ScreenDateTime` to `CAMDateTime` |
| `CAMToOrderSetInHr`     | Duration in hours (2 decimals) from `CAMDateTime` to `OrderSetDateTime` (can be negative, 0, null, or positive) |

---

## 3. Delirium Episode Summary

- Each patient can have 0 to 3 delirium episodes (`CAM=1` followed immediately by `CAM=2`)
- Only the **first** such episode is captured in this dataset
- If no such episode exists, the related fields are left blank or set to `0`

| Column                | Description |
|-----------------------|-------------|
| `CAMDateTime`         | Timestamp of the first CAM assessment after admission (`CAM=0`, `1`, or `2`); must not be null |
| `DateTimeSuspected`   | Timestamp of first `CAM=1` that is immediately followed by `CAM=2`; must be the same or later than `CAMDateTime` |
| `AcquiredUnit`        | Unit where the patient was located when `CAM=1` was recorded for a confirmed delirium episode. Format: `FacID` + unit code (e.g., `H001-2B`) |
| `AvgDeliriumDaysInHr` | Average duration in hours (2 decimals) across all 3 episodes (`0` if none) |

---

## 4. Risk and Confirmation

| Column                | Description |
|-----------------------|-------------|
| `RiskOfDelirium`      | Always `1` (all patients are considered at risk) |
| `ConfirmedDelirium`   | `1` if `DateTimeSuspected` is not null, else `0` |

---

## 5. Contributing Medication

| Column                        | Description |
|-------------------------------|-------------|
| `ContributingMedication`      | Randomly assigned from `'Medication 1'` to `'Medication 10'` or left null |
| `ContributingMedicationDateTime` | Timestamp of medication order (must be between `ArrDateTime` and `DisDateTime`; null if medication is null) |

---

## 6. Demographics

| Column      | Description |
|-------------|-------------|
| `AgeGroup`  | Random from: `'35-44'`, `'45-54'`, `'55-64'`, `'65-74'`, `'75-84'`, `'85-94'`, `'95+'` |

---

## Project Overview

This synthetic dataset was created to support a Power BI dashboard focused on summarizing the first delirium episode per admitted patient. It is designed for data analysts, healthcare researchers, and students who want to explore and analyze patient data related to delirium episodes.

---

## Files Included

| File Name           | Description |
|---------------------|-------------|
| `EDMADMCombined.csv` | Base patient encounter and demographic data |
| `Delirium.csv`       | Subset of patients with delirium screening and episode data |
| `DeliriumAI.csv`     | Subset of patients with AI-predicted delirium risk data |

---

## Data Dictionary

### EDMADMCombined

| Column                       | Description |
|------------------------------|-------------|
| `URN`                        | Unique patient ID (e.g., `P0001–P5000`) |
| `Age`                        | Patient's age (17 years or older) |
| `AgeGroup`                   | Age group based on `Age` |
| `FacID`                      | Random hospital facility ID from `H001–H003` |
| `ArrDateTime`                | Date + time the patient arrived |
| `AdmDateTime`                | Date + time admitted to inpatient unit |
| `DisDateTime`                | Date + time of discharge |
| `Admitted`                   | Always `1` (admitted patients only) |
| `LOS`                        | Length of stay in days (2 decimals) |
| `Expired`                    | 5% chance a patient dies during visit (`1 = yes`, `0 = no`) |
| `RiskOfDelirium`             | Any overlapped URN on Delirium table is `1`, else `0` |
| `ConfirmedDelirium`          | Any overlapped URN on Delirium table whose `FirstDateTimeSuspected` is not null is `1`, else `0` |
| `ContributingMedication`     | Randomly assigned from `'Medication 1'` to `'Medication 10'` or left null |
| `ContributingMedicationDateTime` | Timestamp of medication order |
| `FirstOrderSetDateTime`      | Timestamp of earliest delirium order set placement |
| `OrderSetFlag`               | `1` if order set is given, else `0` |

### Delirium

| Column                       | Description |
|------------------------------|-------------|
| `URN`                        | Unique patient ID (e.g., `P0001–P5000`) |
| `FirstScreenDateTime`        | Optional timestamp for pre-screening |
| `ScreenFlag`                 | `1` if pre-screen occurred, else `0` |
| `CAM`                        | Ranged from `0` for Incomplete, `1` for Delirium Suspected, and `2` for Delirium Not Suspected |
| `CAMDateTime`                | Timestamp of the first CAM assessment after admission |
| `ScreenToCAMInHr`            | Duration in hours from `FirstScreenDateTime` to `CAMDateTime` |
| `CAMToOrderSetInHr`          | Duration in hours from `CAMDateTime` to `FirstOrderSetDateTime` |
| `FirstDateTimeSuspected`     | Timestamp of first `CAM=1` that is immediately followed by `CAM=2` |
| `AcquiredUnit`               | Unit where the patient was located when `FirstDateTimeSuspected` was recorded |
| `AvgDeliriumDaysInHr`        | Average duration in hours across all 3 episodes |

### DeliriumAI

| Column                       | Description |
|------------------------------|-------------|
| `URN`                        | Unique patient ID (e.g., `P0001–P5000`) |
| `FirstPredictedDateTime`     | Timestamp of the first AI algorithm model run for a patient |
| `FirstDateTimePredictedRisk` | Optional timestamp of the AI algorithm model predicting a patient is at risk of delirium |
| `AcquiredUnit`               | Unit where the patient was located when `FirstDateTimePredictedRisk` was recorded |
| `AvgDeliriumDaysInHr`        | Average duration in hours across all 3 episodes |

---

## How to Reproduce the Datasets

To reproduce the synthetic patient datasets, you can use the provided Python script 🐍 `generate_datasets.py`. This script generates the 📊 `EDMADMCombined`, 📊 `Delirium`, and 📊 `DeliriumAI` datasets based on the specifications outlined above.

### Steps:

1. Ensure you have Python installed on your machine.
2. Install the required libraries: `pandas`, `numpy`, `random`, `datetime`.
3. Run the `generate_datasets.py` script.

