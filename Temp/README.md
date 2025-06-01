
# Synthetic Patient Dataset Generation

This repository contains synthetic patient datasets for a Power BI project. The datasets are designed to simulate patient data for the purpose of analyzing delirium and related metrics. The datasets include `Delirium`, `DeliriumAI`, and `EDMADMCombined` tables.

## Dataset Purpose

The purpose of these datasets is to provide a realistic simulation of patient data for the analysis of delirium, its prediction, and related metrics. The datasets can be used to create visualizations, perform data analysis, and build predictive models in Power BI.

## Dataset Structure

### Delirium Table

| Column Name             | Column Description                                                                 |
|-------------------------|-------------------------------------------------------------------------------------|
| URN                     | Unique patient ID (e.g., P0001–P5000)                                               |
| FirstScreenDateTime     | Optional timestamp for pre-screening (must be between ArrDateTime and AdmDateTime)  |
| ScreenFlag              | 1 if pre-screen occurred, else 0                                                    |
| CAM                     | Ranged from 0 for Incomplete, 1 for Delirium Suspected, and 2 for Delirium Not Suspected |
| CAMDateTime             | Timestamp of the first CAM assessment after admission (CAM=0, 1, or 2); must not be null |
| ScreenToCAMInHr         | Duration in hours (2 decimals) from FirstScreenDateTime to CAMDateTime (can be negative, 0, null, or positive) |
| CAMToOrderSetInHr       | Duration in hours (2 decimals) from CAMDateTime to FirstOrderSetDateTime (can be negative, 0, null, or positive) |
| FirstDateTimeSuspected  | Timestamp of first CAM=1 that is immediately followed by CAM=2; must be the same or later than CAMDateTime |
| AcquiredUnit            | Unit where the patient was located when FirstDateTimeSuspected was recorded for a confirmed delirium episode. Format: FacID + unit code (e.g., H001-2B); Unit Code can be as following: 1A, 1B, 1C, 2A, 2B, 2C, 3A, 3B, 3C |
| AvgDeliriumDaysInHr     | Average duration in hours (2 decimals) across all 3 episodes (0 if none)            |

### DeliriumAI Table

| Column Name             | Column Description                                                                 |
|-------------------------|-------------------------------------------------------------------------------------|
| URN                     | Unique patient ID (e.g., P0001–P5000)                                               |
| FirstPredictedDateTime  | Timestamp of the first AI algorithm model run for a patient to predict the probability of risk of this patient to be a delirium patient after admission (0-100%); must not be null |
| FirstDateTimePredictedRisk | Optional timestamp of the AI algorithm model predicts a patient is at risk of delirium after admission; must be the same or later than FirstPredictedDateTime |
| AcquiredUnit            | Unit where the patient was located when FirstDateTimePredictedRisk was recorded for a confirmed delirium episode. Format: FacID + unit code (e.g., H001-2B); Unit Code can be as following: 1A, 1B, 1C, 2A, 2B, 2C, 3A, 3B, 3C |
| AvgDeliriumDaysInHr     | Average duration in hours (2 decimals) across all 3 episodes (0 if none)            |

### EDMADMCombined Table

| Column Name             | Column Description                                                                 |
|-------------------------|-------------------------------------------------------------------------------------|
| URN                     | Unique patient ID (e.g., P0001–P5000)                                               |
| Age                     | A patient's age that is 17 years or older                                           |
| AgeGroup                | Ranged from: '35-44', '45-54', '55-64', '65-74', '75-84', '85-94', '95+' based on Age |
| FacID                   | Random hospital facility ID from H001–H003                                          |
| ArrDateTime             | Date + time the patient arrived (this timestamp is to be the earliest timestamp in this patient's journey) |
| AdmDateTime             | Date + time admitted to inpatient unit (must be after ArrDateTime)                  |
| DisDateTime             | Date + time of discharge (must be after AdmDateTime)                                |
| Admitted                | Always 1 (admitted patients only)                                                   |
| LOS                     | Length of stay in days (2 decimals), calculated as DisDateTime - AdmDateTime        |
| Expired                 | 5% chance a patient dies during visit (1 = yes, 0 = no)                             |
| RiskOfDelirium          | Any overlapped URN on Delirium table is 1, else 0                                   |
| ConfirmedDelirium       | Any overlapped URN on Delirium table whose FirstDateTimeSuspected is not null is 1, else 0 |
| ContributingMedication  | Optional timestamp of medication order (must be between ArrDateTime and DisDateTime; null if medication is null) |
| ContributingMedicationDateTime | Randomly assigned from 'Medication 1' to 'Medication 10' or left null        |
| FirstOrderSetDateTime   | Optional timestamp of earliest delirium order set placement (must be after ScreenDateTime if both exist) |
| OrderSetFlag            | 1 if order set is given, else 0                                                     |

## Dataset Generation Logic

1. **EDMADMCombined Table**:
   - Generate 5,000 unique patient records with realistic timestamps and values.
   - Ensure logical consistency between `ArrDateTime`, `AdmDateTime`, and `DisDateTime`.

2. **Delirium Table**:
   - Randomly select 2,500 URNs from `EDMADMCombined`.
   - Generate the rest of the columns based on the selected URNs.

3. **DeliriumAI Table**:
   - Randomly select 2,500 URNs from `EDMADMCombined`.
   - Generate the rest of the columns based on the selected URNs.

## Usage for Power BI Projects

1. **Import the datasets** into Power BI.
2. **Create relationships** between the tables using the `URN` column.
3. **Build visuals and dashboards** to analyze delirium metrics, predict risk, and explore patient data.

## Example Visuals

- **Delirium Incidence**: Visualize the number of patients with confirmed delirium episodes.
- **Risk Prediction**: Analyze the accuracy of AI predictions for delirium risk.
- **Length of Stay**: Explore the length of stay for patients with and without delirium.

## Conclusion

These synthetic datasets provide a realistic simulation of patient data for analyzing delirium and related metrics. 
They are designed to be used in Power BI projects to create insightful visualizations and predictive models 📊.

---
