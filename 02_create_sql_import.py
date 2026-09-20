import pandas as pd

csv_path = r"C:\Users\aggar\OneDrive\Desktop\Company-Insights-360\data\Sample_Superstore.csv"
sql_path = r"C:\Users\aggar\OneDrive\Desktop\Company-Insights-360\sql\superstore_import.sql"

df = pd.read_csv(csv_path)

# Convert dates correctly: original Superstore format is MM/DD/YY
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="mixed", dayfirst=True
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="mixed", dayfirst=True
)

def sql_value(value):
    if pd.isna(value):
        return "NULL"

    if isinstance(value, str):
        value = value.replace("\\", "\\\\")
        value = value.replace("'", "''")
        return f"'{value}'"

    return str(value)

columns = [
    "row_id", "order_id", "order_date", "ship_date",
    "ship_mode", "customer_id", "customer_name", "segment",
    "country", "city", "state", "postal_code", "region",
    "product_id", "category", "sub_category", "product_name",
    "sales", "quantity", "discount", "profit"
]

with open(sql_path, "w", encoding="utf-8") as f:

    f.write("USE company_insights_360;\n\n")

    f.write("TRUNCATE TABLE superstore_sales;\n\n")

    batch_size = 500

    for start in range(0, len(df), batch_size):

        batch = df.iloc[start:start + batch_size]

        f.write(
            "INSERT INTO superstore_sales (" +
            ", ".join(columns) +
            ") VALUES\n"
        )

        rows = []

        for _, row in batch.iterrows():

            values = [
                row["Row ID"],
                row["Order ID"],
                row["Order Date"].strftime("%Y-%m-%d"),
                row["Ship Date"].strftime("%Y-%m-%d"),
                row["Ship Mode"],
                row["Customer ID"],
                row["Customer Name"],
                row["Segment"],
                row["Country"],
                row["City"],
                row["State"],
                row["Postal Code"],
                row["Region"],
                row["Product ID"],
                row["Category"],
                row["Sub-Category"],
                row["Product Name"],
                row["Sales"],
                row["Quantity"],
                row["Discount"],
                row["Profit"]
            ]

            rows.append(
                "(" + ", ".join(sql_value(v) for v in values) + ")"
            )

        f.write(",\n".join(rows))
        f.write(";\n\n")

print("SQL import file created successfully.")
print("Rows:", len(df))
print("File:", sql_path)