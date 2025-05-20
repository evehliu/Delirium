
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

| Column       | Description |
|--------------|-------------|
| `FacID`      | Random hospital facility ID from `H001–H003` |
| `URN`        | Unique patient ID (e.g., `P0001–P5000`) |
| `ArrDateTime` | Date + time the patient arrived |
| `AdmDateTime` | Date + time admitted to inpatient unit |
| `DisDateTime` | Date + time of discharge (must be after `AdmDateTime`) |
| `Admitted`   | Always `1` (admitted only) |
| `LOS`        | Length of stay in days (2 decimals), calculated as `DisDateTime - AdmDateTime` |
| `Expired`    | 5% chance a patient dies during visit (`1 = yes`, `0 = no`) |

---

## 2. Screening and Order Set Metadata

| Column               | Description |
|----------------------|-------------|
| `ScreenDateTime`     | Optional timestamp for pre-screening (must be between `ArrDateTime` and `AdmDateTime`) |
| `ScreenFlag`         | `1` if pre-screen occurred, else `0` |
| `OrderSetDateTime`   | Timestamp of earliest delirium order set placement (must be after `ScreenDateTime` if both exist) |
| `OrderSetFlag`       | `1` if order set occurred, else `0` |
| `ScreenToCAMInHr`  | Duration in hours (2 decimals) from `ScreenDateTime` to `CAMDateTime` |
| `CAMToOrderSetInHr`| Duration in hours (2 decimals) from `CAMDateTime` to `OrderSetDateTime` (can be negative, 0, null, or positive) |

---

## 3. Delirium Episode Summary

- Each patient can have 0 to 3 delirium episodes (`CAM=1` followed immediately by `CAM=2`)  
- Only the **first** such episode is captured in this dataset  
- If no such episode exists, the related fields are left blank or set to `0`  

| Column              | Description |
|---------------------|-------------|
| `CAMDateTime`       | Timestamp of the first CAM assessment after admission (`CAM=0`, `1`, or `2`); must not be null |
| `DateTimeSuspected` | Timestamp of first `CAM=1` that is immediately followed by `CAM=2`; must be the same or later than `CAMDateTime` |
| `AcquiredUnit` | Unit where the patient was located when `CAM=1` was recorded for a confirmed delirium episode. Format: `FacID` + unit code (e.g., `H001-2B`) |
| `AvgDeliriumDaysInHr` | Average duration in hours (2 decimals) across all 3 episodes (`0` if none) |

---

## 4. Risk and Confirmation

| Column             | Description |
|--------------------|-------------|
| `RiskOfDelirium`   | Always `1` (all patients are considered at risk) |
| `ConfirmedDelirium`| `1` if `DateTimeSuspected` is not null, else `0` |

---

## 5. Contributing Medication

| Column                      | Description |
|-----------------------------|-------------|
| `ContributingMedication`    | Randomly assigned from `'Medication 1'` to `'Medication 10'` or left null |
| `ContributingMedicationDateTime` | Timestamp of medication order (must be between `ArrDateTime` and `DisDateTime`; null if medication is null) |

---

## 6. Demographics

| Column     | Description |
|------------|-------------|
| `AgeGroup` | Random from: `'35-44'`, `'45-54'`, `'55-64'`, `'65-74'`, `'75-84'`, `'85-94'`, `'95+'` |

---
