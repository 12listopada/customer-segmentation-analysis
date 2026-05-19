import pandas as pd

rfm = pd.read_csv('data/processed/rfm_scores.csv')

# Granice na podstawie statystyk ktore widzialysmy
# Recency: mediana = 51, srednia = 92
# Frequency: mediana = 2, srednia = 4
# Monetary: mediana = 674

def assign_segment(row):
    r = row['Recency']
    f = row['Frequency']
    m = row['Monetary']
    
    if r <= 51 and f >= 4 and m >= 674:
        return 'Champion'
    elif r <= 92 and f >= 2:
        return 'Loyal'
    elif r > 92 and f >= 4:
        return 'At Risk'
    elif r <= 51 and f == 1:
        return 'New Customer'
    elif r <= 92 and f == 1:
        return 'Promising'
    else:
        return 'Lost'

rfm['Segment'] = rfm.apply(assign_segment, axis=1)

print("Rozklad segmentow:")
print(rfm['Segment'].value_counts())

print("\nSrednie RFM per segment:")
print(rfm.groupby('Segment')[['Recency','Frequency','Monetary']].mean().round(1))

# Zapisz
rfm.to_csv('data/processed/rfm_segmented.csv', index=False)
print("\nZapisano!")