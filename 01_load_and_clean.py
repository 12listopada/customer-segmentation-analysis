import pandas as pd

# Wczytaj dane
# header=0 oznacza ze pierwszy wiersz to naglowki kolumn
df = pd.read_excel('data/raw/Online_Retail.xlsx', header=0)

print("Pierwsze 5 wierszy:")
print(df.head())

print("\nKolumny:")
print(df.columns.tolist())

print("\nRozmiar danych:")
print(df.shape)

print("\nBrakujace wartosci:")
print(df.isnull().sum())
# Usun wiersze bez CustomerID - nie wiemy kto kupil
df = df.dropna(subset=['CustomerID'])
print(f"\nPo usunieciu brakujacych CustomerID: {df.shape}")

# Usun zwroty (InvoiceNo zaczyna sie od 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
print(f"Po usunieciu zwrotow: {df.shape}")

# Usun ujemne ilosci i ceny zerowe
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
print(f"Po usunieciu ujemnych: {df.shape}")

# Dodaj kolumne TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Zmien CustomerID na int
df['CustomerID'] = df['CustomerID'].astype(int)

print("\nPo czyszczeniu:")
print(df.head())
print(df.shape)

# Zapisz
df.to_csv('data/processed/retail_clean.csv', index=False)
print("\nZapisano!")
# Dodaj to na końcu pliku żeby sprawdzić
customer_check = df[df['CustomerID'] == 17850]
print(f"\nKlient 17850:")
print(f"Liczba zamowien: {customer_check['InvoiceNo'].nunique()}")
print(f"Ostatni zakup: {customer_check['InvoiceDate'].max()}")
print(f"Suma wydatkow: {customer_check['TotalPrice'].sum():.2f}")

