import pandas as pd
import sqlite3  

conn = sqlite3.connect('data/processed/customer_segmentation.db')

queries = {
    'segment_summary': """
        SELECT 
            Segment,
            COUNT(*) as customer_count,
            ROUND(AVG(Recency), 1) as avg_recency,
            ROUND(AVG(Frequency), 1) as avg_frequency,
            ROUND(AVG(Monetary), 1) as avg_monetary,
            ROUND(SUM(Monetary), 1) as total_revenue
        FROM rfm_segments
        GROUP BY Segment
        ORDER BY avg_monetary DESC
    """,
    'top_champions': """
        SELECT CustomerID, Recency, Frequency, ROUND(Monetary, 2) as Monetary
        FROM rfm_segments
        WHERE Segment = 'Champion'
        ORDER BY Monetary DESC
        LIMIT 10
    """,
    'lost_vs_champion': """
        SELECT 
            Segment,
            COUNT(*) as customers,
            ROUND(AVG(Monetary), 1) as avg_spend,
            ROUND(MIN(Monetary), 1) as min_spend,
            ROUND(MAX(Monetary), 1) as max_spend
        FROM rfm_segments
        WHERE Segment IN ('Champion', 'Lost')
        GROUP BY Segment
    """
}

for name, query in queries.items():
    df = pd.read_sql(query, conn)
    df.to_csv(f'data/processed/{name}.csv', index=False)
    print(f"\n{name}:")
    print(df)

conn.close()
print("\nGotowe!")