import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Setting a random seed for consistent results
np.random.seed(42)

# =====================================================================
# 1. GENERATE DIMENSION: DATA CLUSTERS
# =====================================================================
clusters_data = {
    'cluster_id': ['CLS-CORE-BANK', 'CLS-EQ-TRADE', 'CLS-FX-MATH', 'CLS-CUST-MD'],
    'cluster_name': ['Core Banking Ledger', 'Equities Trading Engine', 'Forex Matching Platform', 'Customer Master Data'],
    'data_criticality': ['Tier-1 (Critical)', 'Tier-1 (Critical)', 'Tier-2 (High)', 'Tier-3 (Medium)']
}
df_clusters = pd.DataFrame(clusters_data)
df_clusters.to_csv('dim_data_clusters.csv', index=False)

# =====================================================================
# 2. GENERATE DIMENSION: DATABASE NODES
# =====================================================================
nodes_data = {
    'node_id': ['DB-NY-PRI', 'DB-LDN-REP', 'DB-MUM-REP', 'DB-TKY-REP'],
    'node_name': ['New York Primary', 'London Replica', 'Mumbai Replica', 'Tokyo Replica'],
    'region': ['US-East (New York)', 'UK-South (London)', 'AP-South (Mumbai)', 'AP-Northeast (Tokyo)'],
    'node_role': ['Primary', 'Replica', 'Replica', 'Replica'],
    'db_engine': ['PostgreSQL High-Avail', 'PostgreSQL Replica', 'PostgreSQL Replica', 'PostgreSQL Replica']
}
df_nodes = pd.DataFrame(nodes_data)
df_nodes.to_csv('dim_database_nodes.csv', index=False)

# =====================================================================
# 3. GENERATE FACT TABLE: REPLICATION METRICS (With Real-World Anomalies)
# =====================================================================
# We will generate 24 hours of data taken every 5 minutes
start_time = datetime(2026, 6, 13, 0, 0, 0)
timestamps = [start_time + timedelta(minutes=5 * i) for i in range(288)] # 288 intervals in a day

fact_rows = []

for ts in timestamps:
    # Introduce a specific "Network Incident" story between 14:00 and 15:30
    is_incident_time = (ts.hour == 14) or (ts.hour == 15 and ts.minute <= 30)

    for cluster_id in df_clusters['cluster_id']:
        for node_id in df_nodes['node_id']:
            # Primary nodes do not have replication lag relative to themselves
            if node_id == 'DB-NY-PRI':
                lag = 0
                failures = 0
                throughput = np.random.uniform(80, 120)
            else:
                # Standard baseline operations (Healthy state)
                if not is_incident_time:
                    lag = np.random.exponential(scale=15) + np.random.uniform(5, 15)  # Healthy lag: 5 to 40 ms
                    failures = np.random.choice([0, 1], p=[0.98, 0.02])              # Very rare minor failures
                    throughput = np.random.uniform(40, 70)

                # Incident Scenario: Transatlantic fiber cable degradation affecting London replica
                else:
                    if node_id == 'DB-LDN-REP' and cluster_id == 'CLS-EQ-TRADE':
                        lag = np.random.uniform(1500, 3500)      # Massively spiked lag: 1.5 to 3.5 seconds!
                        failures = np.random.randint(5, 15)       # High sync failures
                        throughput = np.random.uniform(5, 15)     # Drop in data throughput
                    else:
                        # Other regions experience slight collateral lag due to queue backups
                        lag = np.random.exponential(scale=50) + 30
                        failures = np.random.choice([0, 1], p=[0.95, 0.05])
                        throughput = np.random.uniform(35, 65)

            # High-priority clusters handle a higher volume of transactions
            if cluster_id in ['CLS-CORE-BANK', 'CLS-EQ-TRADE']:
                tx_count = np.random.randint(1500, 3000)
            else:
                tx_count = np.random.randint(300, 800)

            fact_rows.append({
                'timestamp': ts.strftime('%Y-%m-%d %H:%M:%S'),
                'cluster_id': cluster_id,
                'node_id': node_id,
                'replication_lag_ms': round(lag, 2),
                'transactions_processed': tx_count,
                'sync_failure_count': failures,
                'bandwidth_consumed_mbps': round(throughput, 2)
            })

df_fact = pd.DataFrame(fact_rows)
df_fact.to_csv('fact_replication_metrics.csv', index=False, encoding = "utf-8")

print("All 3 clean Star Schema datasets successfully generated!")
