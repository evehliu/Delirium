
# Delirium Dashboard Portfolio

## 📊 Types of Data Visualizations

### Interactive Dashboards

**Figure 1: Dashboard Wireframe**

1. **Highlight Card**  
   - Displays high-level KPIs for the selected period vs. the latest fiscal period.  
   - Conditional formatting:  
     - 🟦 Teal = Positive outcome (higher is better)  
     - 🟧 Orange = Negative outcome (higher is worse)  
   - Interactions disabled to maintain focus.

2. **Period Selection**  
   - Options: Day (latest completed), Fiscal Week, Quarter, Year  
   - Implemented via Parameter–Bookmark combo to avoid duplicating visuals/pages.

3. **Toggle**  
   - **Patient Toggle**: Admitted vs. non-admitted data  
   - **Date Selector Toggle**: Hides selector to reduce query load and focus on default view.

4. **Definition-Interpretation Tooltip**  
   - Explains metric calculations  
   - Content sourced from Excel, editable without Power BI Desktop.

5. **Bookmarks-Linked Button**  
   - Switch views (e.g., Community vs. Hospital, Pharmaceutical vs. PRISME)  
   - Syncs visual states (e.g., all age-related visuals shown when 'Age' is selected).

6. **Customized Data Label Value**  
   - Percentages include numerator/denominator  
   - Site launch date highlighted for context.

7. **Drill Through**  
   - Access patient-level details  
   - Standardized layout for readability.

8. **Role-Level Security (RLS)**  
   - Custom measure restricts access to drill-through pages  
   - Main dashboard access via distribution group.

---

## 📖 Storytelling with Data

### Delirium Incidence Rate  
- **Visualization**: Bar + line charts  
- **Filters**: Acquisition method, period, site/unit  
- **Use Case**: Hot Spot Analysis for Hospital-Acquired Delirium (HAD)

### Utilized Treatment: Pharmaceutical vs. PRISME  
- **Visualization**:  
  - Stacked bar charts for 4 patient groups  
  - Clustered stacked bar for PRISME factor distribution  
- **Use Case**: Evaluate PRISME Framework effectiveness

### Prior Drugs Used in Patients at Risk  
- **Visualization**: Bar charts with drill-through  
- **Use Case**: Monitor prescriptions, especially for elderly inpatients

### Screening Method: CAM vs. AI  
- **Visualization**: Stacked bar chart  
- **Use Case**: Identify detection gaps, prioritize early intervention

### Most Relevant AI Driving Factor  
- **Visualization**: Top 5 AI factors with percentage labels  
- **Use Case**: Support early diagnosis

### CAM Completion Rate  
- **Visualization**:  
  - Horizontal segmented bar (completed vs. incomplete)  
  - Line chart for trends  
- **Use Case**: Ensure consistent screening and monitoring

---

## 📈 Charts & Graphs

- Simplified visuals to reduce cognitive load  
- Mix of clustered/stacked bar charts and line charts  
- Enhances clarity and decision-making

---

## 🧮 Use of DAX and Power Query

### DAX
- `USERELATIONSHIP`: Activates inactive relationships  
- `ALL`: Ignores filters for total row counts  
- `UNION`, `SELECTCOLUMNS`, `FILTER`: Combine and deduplicate data  
- **Custom RLS Measure**: Access control by user email/unit

### Power Query
- Transforms DeliriumAI dataset  
- Prepares SHAP features/values  
- Merges, unpivots, splits, and aggregates data

---

## 🧠 How I Structure and Present Analytical Findings

### Clear Hierarchy & Layout
- **Sections**:  
  1. Location Analysis  
  2. Trend Analysis  
  3. Contributing Factors (CAM, AI, PRISME)

### Data-Driven Decision Making
- Influences decisions on high-risk units and treatment protocols  
- Highlights hospital harm stats and orderset effectiveness

### Annotations & Contextual Insights
- Tooltips, icons, titles, legends, axis labels  
- Consistent color codes

---

## 🧑‍💻 My Approach to Making Data Accessible and Actionable

### User-Centered Design
- Tailored for clinical, operational, and quality stakeholders  
- Visual flow: High-level → Granular (site → unit → patient)

### Optimized Performance
- **Data Model**: Star schema  
- **Data Volume**: Irrelevant data removed early  
- **DAX**: Efficient measures, transformations in Power Query  
- **Cardinality**: Single-direction relationships, avoid high-cardinality slicers

### Integration with Business Process
- Tracks key metrics (e.g., orderset utilization, mortality)  
- Triggers alerts/tasks via Power Automate

### Accessibility Consideration
- Clear labels, consistent colors, structured layouts  
- In-progress improvements:  
  - WCAG-compliant contrast  
  - Alt text for screen readers  
  - Keyboard navigation
