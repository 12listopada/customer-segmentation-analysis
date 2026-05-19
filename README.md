# Customer Segmentation Analysis

RFM-based customer segmentation of 4,338 retail customers using Python, SQL and Power BI.  
**Key finding:** Champions represent 26% of customers but generate 70% of total revenue — 9x more than Lost customers.

---

## Business Problem

Retail businesses often treat all customers the same — same emails, same discounts, same campaigns. This project segments customers by actual behaviour to answer: **who are the most valuable customers, and what should the business do differently for each group?**

---

## Tools & Stack

| Tool | Purpose |
|------|---------|
| Python (pandas) | Data cleaning, RFM calculation, segmentation |
| SQL (SQLite) | Data storage and aggregation queries |
| Power BI + DAX | Interactive dashboard and visualisation |
| Git / GitHub | Version control |

---

## Dataset

- **Source:** UCI Online Retail Dataset
- **Scope:** 4,338 customers, transactions from 2010–2011
- **Currency:** GBP (£)

---

## Methodology — RFM Segmentation

RFM stands for **Recency, Frequency, Monetary** — three behavioural dimensions used to score and segment customers.

| Dimension | Definition |
|-----------|-----------|
| Recency | Days since last purchase (lower = better) |
| Frequency | Number of orders placed |
| Monetary | Total revenue generated (£) |

Each customer received an RFM score and was assigned to one of **6 segments**:

| Segment | Description |
|---------|-------------|
| 🏆 Champion | Bought recently, buys often, spends the most |
| 💛 Loyal | Regular buyers with consistent spend |
| ⚠️ At Risk | Previously frequent buyers who haven't returned |
| 🔵 Promising | Recent buyers with low frequency — growth potential |
| 🆕 New Customer | First-time buyers in the last 30 days |
| ❌ Lost | Inactive for 220+ days, low frequency |

---

## Key Findings

- **Champions (26% of customers) generate £6.2M — 70% of total revenue**
- **Lost customers (30% of customers) generate only £780K**
- Champion avg spend: **£5,524** vs Lost avg spend: **£604** — a **9x difference**
- At Risk customers have high historical frequency (avg 5.4 orders) but haven't purchased in 155 days on average — strong re-engagement potential

---

## Project Structure

```
customer-segmentation-analysis/
│
├── data/
│   ├── raw/                        # Original dataset
│   └── processed/
│       └── customer_segmentation.db  # SQLite database
│
├── 01_load_and_clean.py            # Load data, handle nulls, remove cancellations
├── 02_rfm_calculation.py           # Calculate Recency, Frequency, Monetary per customer
├── 03_segmentation.py              # Assign RFM scores and segment labels
├── 04_load_to_sqlite.py            # Load segmented data into SQLite
├── 05_run_sql.py                   # Run SQL aggregation queries
└── README.md
```

---

## Pipeline — Step by Step

### `01_load_and_clean.py`
- Load raw Excel file
- Remove rows with null CustomerID
- Remove cancelled transactions (InvoiceNo starting with 'C')
- Remove negative quantities and unit prices
- Create `TotalPrice` column (Quantity × UnitPrice)

### `02_rfm_calculation.py`
- Set reference date as max invoice date + 1 day
- Calculate Recency (days since last purchase)
- Calculate Frequency (number of unique invoices)
- Calculate Monetary (sum of TotalPrice per customer)

### `03_segmentation.py`
- Score each RFM dimension on a 1–4 scale using quartiles
- Combine scores into RFM rules to assign segment labels
- Output: 6 segments for 4,338 customers

### `04_load_to_sqlite.py`
- Load segmented data into SQLite database
- Create three tables: `rfm_segmented`, `segment_summary`, `lost_vs_champion`

### `05_run_sql.py`
- Run aggregation queries: avg spend, total revenue, recency and frequency per segment
- Output results to console for validation

---

## Power BI Dashboard

Two-page interactive dashboard built in Power BI Desktop.

**Page 1 — Segment Overview**
- 5 KPI cards: Total Customers, Champions, Lost Customers, Champion Revenue, Lost Revenue
- Customer Distribution donut chart
- Average Spend by Segment bar chart
- Recency vs Frequency comparison chart
- Business insight callouts
  <img width="2045" height="1150" alt="Zrzut ekranu 2026-05-19 191543" src="https://github.com/user-attachments/assets/b5d3cf97-0d35-4f86-a2ae-773d25b5b259" />


**Page 2 — Segment Action Plan**
- Top 10 Champions by Revenue (CustomerID, Recency, Frequency, Monetary)
- Total Revenue by Segment bar chart
- Recommended business actions per segment
<img width="2042" height="1150" alt="Zrzut ekranu 2026-05-19 191618" src="https://github.com/user-attachments/assets/e37edd51-6a37-4166-a4ef-c53b1facf4c7" />

---

## Business Recommendations

| Segment | Recommended Action |
|---------|-------------------|
| 🏆 Champion | Reward with loyalty programme, exclusive offers, early product access |
| 💛 Loyal | Upsell premium products, increase frequency with targeted bundles |
| ⚠️ At Risk | Re-engagement campaign with personalised discounts — act before they go Lost |
| 🔵 Promising | Second purchase incentive, nurture email sequence |
| 🆕 New Customer | 90-day onboarding sequence, welcome campaign |
| ❌ Lost | Last-chance win-back offer — if no response, archive |

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/12listopada/customer-segmentation-analysis.git
cd customer-segmentation-analysis

# Install dependencies
pip install pandas openpyxl

# Run the pipeline in order
python 01_load_and_clean.py
python 02_rfm_calculation.py
python 03_segmentation.py
python 04_load_to_sqlite.py
python 05_run_sql.py
```

Then open the Power BI `.pbix` file and refresh the data connection to `data/processed/customer_segmentation.db`.

---

## Author

**Oliwia** — Data Analyst  
[GitHub](https://github.com/12listopada)
