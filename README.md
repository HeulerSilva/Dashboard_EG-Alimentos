# 📊 Dashboard de Vendas Interativo — EG Alimentos

> Interactive sales analytics dashboard built for real-time KPI monitoring, extracting live data from a production SQL Server database.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-heulersilva-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/heulersilva)
[![GitHub](https://img.shields.io/badge/GitHub-HeulerSilva-181717?style=flat&logo=github&logoColor=white)](https://github.com/HeulerSilva)

---

## 🧭 Overview

Data Engineering project focused on extraction (SQL Server), transformation (Pandas), and visualization (Streamlit) — built to give EG Alimentos' leadership real-time visibility into sales performance.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat&logo=microsoftsqlserver&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)

## 🚀 Technical Highlights

Built applying Data Engineering & Architecture best practices, with a focus on scalability and security:

1. **Robust ETL Pipeline** — Full extraction flow via SQLAlchemy connecting directly to a SQL Server instance, efficiently processing a real historical database with **45,000+ records**.
2. **Data Wrangling & Normalization** — Heavy use of Pandas for cleaning raw data, including resolving date format conflicts (ISO vs. BR) and enforcing data types to guarantee revenue metric integrity.
3. **Security Architecture** — Environment variables (`python-dotenv`) manage sensitive credentials, ensuring database connection and security information is never exposed in the public repository.
4. **High-Performance Visualization** — Interactive Streamlit interface integrated with dynamic Plotly charts, using data caching (`@st.cache_data`) to optimize performance and reduce database query load.
5. **Applied Business Intelligence** — Multidimensional views and time-based analysis (Year-over-Year / Month-over-Month) to directly support EG Alimentos' strategic decision-making.

## 📈 Business Impact

| Result | Impact |
|--------|--------|
| ⏱️ Reporting cycle | **–60%** generation time |
| ⚙️ Operational & financial efficiency | **+8.02%** |
| 🗄️ Data processed | 45,000+ real historical records |

## 👤 About

**Heuler Ferreira Silva** — Senior Data Engineer | Analytics Architect
15+ years in enterprise data ecosystems · SQL Expert · Modern Data Stack
📍 Brazil (Remote) · [linkedin.com/in/heulersilva](https://linkedin.com/in/heulersilva)
