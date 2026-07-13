# 📊 Sales Analytics Data Warehouse using Snowflake & Power BI

## 🚀 Project Overview

This project demonstrates an end-to-end Sales Analytics Data Warehouse built using **Snowflake**, **Python**, and **Power BI**.

The pipeline extracts raw sales data from a CSV file, validates and uploads it into Snowflake, transforms it into a dimensional data warehouse (Star Schema), and visualizes business insights through interactive Power BI dashboards.

This project follows industry best practices including:

- Modular Python ETL
- Data Validation
- Snowflake Data Warehouse
- Star Schema Design
- Automated Testing
- CI/CD using GitHub Actions
- Interactive Power BI Dashboards

---

## 🏗️ Architecture

```
                CSV Dataset
                     │
                     ▼
           Python ETL Pipeline
                     │
                     ▼
          Snowflake RAW Schema
                     │
                     ▼
        Snowflake STAGING Schema
                     │
                     ▼
          Snowflake MART Schema
                     │
                     ▼
           Power BI Dashboard
```

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Database | Snowflake |
| Data Processing | Pandas |
| Data Warehouse | Star Schema |
| BI Tool | Power BI |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
Sales-Analytics-Snowflake/
│
├── .github/
│   └── workflows/
│       └── pipeline.yml
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── python/
│   ├── app/
│   ├── tests/
│   │   ├── unit/
│   │   └── integration/
│   └── logs/
│
├── sql/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 ETL Workflow

1. Read CSV Dataset
2. Validate Dataset
3. Upload to Snowflake RAW Layer
4. Transform into STAGING Layer
5. Build Dimension Tables
6. Build Fact Table
7. Execute Analytics Queries
8. Visualize Data in Power BI

---

## ❄️ Snowflake Architecture

### RAW Layer

Stores original sales data.

### STAGING Layer

Performs data cleaning and transformation.

### MART Layer

Contains:

- FACT_SALES
- DIM_CUSTOMER
- DIM_PRODUCT
- DIM_LOCATION
- DIM_DATE

---

## 📊 Power BI Dashboards

### Executive Dashboard

- Total Sales
- Total Orders
- Total Customers
- Total Products
- Sales Trend
- Sales by Category
- Sales by Region

### Customer Analytics

- Customer KPIs
- Top Customers
- Sales by Segment
- Customer Distribution

---

## 🧪 Testing

### Unit Tests

- Configuration
- Data Validator

### Integration Tests

- Snowflake Connection
- SQL Execution
- Logger
- Data Upload

---

## ⚙️ CI/CD

GitHub Actions automatically:

- Installs dependencies
- Executes unit tests
- Validates project structure

---

## ▶️ How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute ETL

```bash
cd python
python -m app.etl
```

### Run Unit Tests

```bash
cd python
python -m pytest tests/unit -v
```

### Run Integration Tests

```bash
python -m tests.integration.test_connection
python -m tests.integration.test_execute_sql
python -m tests.integration.test_uploader
```

---

## 📈 Future Enhancements

- Snowflake Streams
- Snowflake Tasks
- Stored Procedures
- Materialized Views
- Role-Based Access Control
- Real-Time Data Ingestion
- Airflow Integration

---

## 👨‍💻 Author

**Tushar Datir**

Computer Engineering Graduate

Python | Snowflake | SQL | Power BI | Data Engineering