Types of Data Visualizations

Interactive Dashboards

(Label on Figure 1: Dashboard Wireframe)

① Highlight Card

Displays high-level KPIs for the selected period compared to the latest fiscal period.

Interactions are disabled to maintain focus.

Conditional formatting: teal for positive outcomes (higher is better), orange for negative (higher is worse).

② Period Selection

Aligned with the organization’s reporting calendar: Day (latest completed), Fiscal Week, Fiscal Quarter, and Fiscal Year.

Implemented using a Parameter–Bookmark combination to avoid duplicating visuals or pages, enhancing interactivity.

③ Toggle

Patient Toggle: Switches between admitted and non-admitted patient data.

Date Selector Toggle: Hides the date selector to reduce query load and guide users to focus on the default view (latest fiscal period).

④ Definition-Interpretation Tooltip

Provides calculation methodology for each metric, complementing the dedicated definitions page within the dashboard.

Content is sourced from a separate Excel workbook, enabling business users to make updates without requiring Power BI Desktop access.

⑤ Bookmarks-Linked Button

Toggles between different data views, such as acquisition types (e.g., Community vs. Hospital) or treatment types (e.g., Pharmaceutical vs. Non-Pharmaceutical, PRISME).

Facilitates navigation, e.g., from ‘Top 5 Contributing Drugs’ to a snapshot of patient age demographics.

Visual state synchronization ensures all relevant age-related visuals are displayed when the 'Age' button is selected.

⑥ Customized Data Label Value

Metrics displayed as percentages are supplemented with the numerator and denominator for clarity.

The site launch date (indicating the start of data availability) is highlighted to provide crucial business context.

⑦ Drill Through

Enables access to patient details relevant to the business context, on a per-visual basis.

Standardized layout across drill-through pages enhances readability.

⑧ Role-Level Security (RLS)

Specific users are granted access to individual drill-through pages for operational purposes via a custom measure.

Main dashboard access is restricted to approved users via a distribution group.

Drill-through pages are accessible only to a subset of those users.

**Figure 1: Dashboard Wireframe**

Storytelling with Data

(Graph on the dashboard)

Delirium Incidence Rate

Visualization: Bar and line charts display the count and rate of delirium incidents, filterable by acquisition method, period, or site/unit.

Use Case: Supported a Hot Spot Analysis for Hospital-Acquired Delirium (HAD), helping identify high-prevalence units and enabling proactive harm reduction.

Utilized Treatment: Pharmaceutical vs. Non-Pharmaceutical (PRISME)

Visualization:

Stacked bar charts and filters explore four patient groups: pharmaceutical only, PRISME only, both, or none, along with their Length of Stay (LOS).

A toggle switches between treatment types.

When PRISME is selected, a clustered stacked bar chart shows the part-to-whole distribution of patients screened by the six PRISME factors.

Use Case: Enabled clinicians to evaluate the PRISME Framework’s effectiveness and refine workflows.

Prior Drugs Used in Patients at Risk of Delirium

Visualization: Bar charts with drill-through functionality highlight medications frequently associated with at-risk patients.

Use Case: Data segmented by acquisition source supports monitoring and prescription adjustments, especially for elderly inpatients.

Screening Method for Delirium: CAM vs. AI

Visualization: A stacked bar chart compares CAM (physician-identified) vs. AI-driven predictions, including overlaps.

Use Case: Helped identify detection gaps and prioritize early intervention for patients flagged by both methods.

Most Relevant AI Driving Factor

Visualization: Highlights the top 5 factors influencing AI predictions, with custom data labels showing percentage usage.

Use Case: Supported early diagnosis by enabling clinicians to monitor current inpatients.

CAM Completion Rate

Visualization: A horizontal segmented bar shows completed vs. incomplete CAM documentation. A line chart tracks utilization trends over time.

Use Case: Helped ensure consistent screening and early detection, establishing a baseline for ongoing monitoring.

Charts & Graphs

Visuals are simplified or de-emphasized where appropriate to reduce cognitive load and guide attention.

A deliberate mix of clustered/stacked bar charts and line charts enhances clarity and decision-making.

Use of DAX and Power Query

DAX

USERELATIONSHIP: Activates inactive relationships (e.g., between ArrAdmTimeDateID and TimeDateID).

ALL: Ignores filters to return total row counts (e.g., in denominator calculations).

UNION, SELECTCOLUMNS, FILTER: Combine insights from multiple tables for row-level filtering and deduplication.

Custom RLS Measure: Implements access control based on user email and unit, with override for developers.

Power Query

Transforms the DeliriumAI dataset to prepare SHAP features and values for analysis.

Merges SHAP feature and value into strings (e.g., feature=0.123), unpivots, splits, and aggregates by date, facility, patient, and feature.

DeliriumAI (example: URN ER0-B20240319131425614)

DeliriumAI+Shap (ER0-B20240319131425614)

How I Structure and Present Analytical Findings

Clear Hierarchy & Layout

The dashboard is constructed with 3 sections:

Location Analysis – High-level summary by hospital site

Trend Analysis – Key metrics on delirium and at-risk patients

Contributing Factors – Includes:

CAM and CAM completion rate

AI and top predictive factors

PRISME and factor-level details

Data-Driven Decision Making

The report influenced decisions like identifying high-risk units and optimizing treatment protocols.

Hospital harm statistics are prominently displayed, followed by orderset utilization comparisons to highlight intervention effectiveness.

Annotations & Contextual Insights

Tooltips: Definitions and icons (e.g., “ⓘ” icons for tooltips)

Descriptions: Titles, legends, axis labels

Color: Consistent hex codes for similar measures

My Approach to Making Data Accessible and Actionable

User-Centered Design

Tailored to stakeholders (clinical, operational, quality improvement).

Visual flow moves from high-level insights to granular details (e.g., site → unit → patient).

Dashboard starts with overall insights (e.g., % of patients at risk, orderset usage). It then drills down into: Location-specific data (e.g., ERH, FCH, MMH, RCH), Unit-level risk, Temporal trends (e.g., fiscal week comparisons), and Patient-level factors (e.g., age, medication history).

Optimized Performance

Data Model: Star schema, minimal relationships

Data Volume: Irrelevant data and unused columns removed early

DAX: Efficient use of FILTER, measures over calculated columns, heavy transformations moved to Power Query

Cardinality: Single-direction relationships, avoid high-cardinality columns in slicers

Integration with Business Process

Tracks key metrics like orderset utilization and mortality impact.

Triggers alerts (e.g., low utilization) or tasks (e.g., missing CAM assessment) via Power Automate.

Accessibility Consideration

Uses clear labels, consistent colors, and structured layouts.

In-progress improvements:

WCAG-compliant color contrast for users with visual impairments.

Alternative text for screen readers and users with low vision

Keyboard navigation and tab order for users who don’t use a mouse