import matplotlib.pyplot as plt
df = pd.read_csv("sales_updated.csv")
df['Region'] = df['Region'].str.strip().str.title()
blazer_rows = df[df['Product'].str.contains('Blazers', case=False, na=False)]
blazer_region = blazer_rows['Region'].dropna().mode()[0]
df.loc[df['Region'].isna() & df['Product'].str.contains('Blazers', case=False, na=False), 'Region'] = blazer_region

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
df['Month'] = df['Date'].dt.month_name()
monthly_sales = df.groupby('Month')['Amount'].sum().sort_values(ascending=False)
print("Month with highest sales:\n", monthly_sales.head(1))

region_sales = df.groupby('Region')['Amount'].sum().sort_values(ascending=False)
region_sales.plot(kind='bar', title='Region-wise Sales')
plt.ylabel("Total Sales")
plt.show()

monthly_sales.plot(kind='bar', title='Month-wise Sales')
plt.ylabel("Total Sales")
plt.show()
