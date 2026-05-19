import pandas as pd

df = pd.read_csv('data/processed/retail_clean.csv')

# Zamien InvoiceDate na date (nie tekst)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Data referencyjna - dzien po ostatniej transakcji
reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
print(f"Data referencyjna: {reference_date}")

# Oblicz RFM dla kazdego klienta
rfm = df.groupby('CustomerID').agg(
    Recency=('InvoiceDate', lambda x: (reference_date - x.max()).days),
    Frequency=('InvoiceNo', 'nunique'),
    Monetary=('TotalPrice', 'sum')
).reset_index()

print("\nRFM - pierwsze 10 klientow:")
print(rfm.head(10))
print(f"\nLiczba unikalnych klientow: {rfm.shape[0]}")

print("\nStatystyki RFM:")
print(rfm.describe())

# Sprawdzenie klienta 17850
print("\nKlient 17850 w RFM:")
print(rfm[rfm['CustomerID'] == 17850])

# Zapisz
rfm.to_csv('data/processed/rfm_scores.csv', index=False)
print("\nZapisano!")
