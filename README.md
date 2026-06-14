# Global Enterprise Ledger & Database Replication Monitor

## 🌐 Project Overview
This repository hosts an enterprise-grade infrastructure operations command terminal designed to monitor real-time data synchronization health and transactional integrity across distributed global banking databases (New York, London, Mumbai, Tokyo). 

The project bridges relational data warehouse architecture with operational risk intelligence by tracking millisecond-level data replication lag, isolating localized infrastructure bottlenecks, and translating technical database system anomalies into corporate SLA business impact indicators.

---

## 📊 Terminal Interface Layout
![Global Ledger Monitor Banner](dashboard_preview.png)

---

## 🛠️ Data Architecture & Pipeline Engineering

The project is built on an end-to-end operational telemetry data pipeline structured as a clean **Star Schema Data Warehouse model**. The underlying relational datasets are dynamically engineered via a vectorized Python pipeline (`main.py`) before consumption by the downstream analytical engine.

### 1. Relational Data Modeling (`main.py`)
* **Dimension Table (`dim_data_clusters.csv`):** Manages metadata across isolated data systems including Core Banking Ledgers, Equities Trading Engines, Forex Matching Platforms, and Customer Master Data, categorizing system criticality tiers.
* **Dimension Table (`dim_database_nodes.csv`):** Controls configuration maps for distributed regional servers (New York Primary, London Replica, Mumbai Replica, Tokyo Replica) tracking deployment environments and database engines.
* **Fact Table (`fact_replication_metrics.csv`):** A high-density time-series data storage layer containing **4,608 synchronized system status records** tracking throughput, failure rates, bandwidth, and millisecond latencies.

### 2. Advanced Telemetry Simulation & Anomaly Injection
* **Vectorized Processing:** Leverages C-optimized `Pandas` and `NumPy` libraries to compute rolling averages, data splits, and tracking metrics instantaneously without utilizing row-by-row iteration loops.
* **Baseline Mathematics:** Uses an exponential random scale distribution (`np.random.exponential(scale=15)`) to map normal, healthy data synchronization properties ranging strictly between **5 ms and 40 ms**.
* **Incident Injection:** Programmatically orchestrates an intense **Transatlantic fiber cable degradation anomaly** between 14:00 and 15:30. The incident injects extreme replication lag ranging up to **3,500 ms (3.5 seconds)** specifically targeting the London Equities Trading node to test downstream system warning barriers.
* **Scale Volume:** Processes over **64 Lakh+ individual financial transactions** (`64,33,294` logged across clusters) to replicate a realistic global financial workload environment.

---

## 🧠 Advanced Analytics & Incident Detection Layer

The visual terminal leverages advanced analytics mechanisms to evaluate the "blast radius" of systemic infrastructure failures on the fly:

* **Fixed Level of Detail (LOD) Calculations:** Deployed immutable expressions to lock global performance baseline parameters bypassing canvas filters:
  `{FIXED [Timestamp] : AVG([Replication Lag Ms])}`
* **Risk Quantification Matrix:** Utilizes conditional table calculations to analyze regional block counts, instantly isolating which node drives transactional gridlock during an ongoing network anomaly.
* **Adjustable SLA Threshold Parameters:** Implemented user-defined rule configurations linked directly to a context-aware Dynamic Header Banner, allowing site reliability engineers to modify corporate threat criteria and risk tiers in real-time.

---

## 📂 Repository Components
* `main.py`: Core Python data architect pipeline managing cross-joins, statistical models, and anomaly injections.
* `dim_data_clusters.csv` / `dim_database_nodes.csv`: Warehouse structural entity dimension datasets.
* `fact_replication_metrics.csv`: Generated high-density operational metrics file.
* `dashboard_preview.png`: High-resolution user interface visual preview.
* `Enterprise Ledger & Distributed Database Replication Workbook`: Packaged workspace configuration compiling primary calculations and dashboards.

---

## 🚀 Key Professional Competencies Demonstrated
* Relational Star Schema Data Warehouse Design
* Time-Series Systems Telemetry Engineering
* Vectorized Array Optimization via Pandas/NumPy
* Business Risk Mapping & Incident Management System Architecture
