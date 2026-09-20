import pandas as pd

# Load dataset
df = pd.read_csv("data/Sample_Superstore.csv")
# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed", dayfirst=True)

print("===== DATASET OVERVIEW =====")
print("Shape:", df.shape)

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print("Duplicate rows:", df.duplicated().sum())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== BUSINESS DATA CHECKS =====")

print("Negative Sales:", (df["Sales"] < 0).sum())
print("Negative Profit:", (df["Profit"] < 0).sum())
print("Zero Sales:", (df["Sales"] == 0).sum())
print("Zero Quantity:", (df["Quantity"] == 0).sum())
print("Discount Range:", df["Discount"].min(), "to", df["Discount"].max())

print("\n===== OVERALL BUSINESS KPIs =====")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
profit_margin = (total_profit / total_sales) * 100

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Profit Margin: {profit_margin:.2f}%")

print("\n===== REGIONAL PERFORMANCE =====")

regional_analysis = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

regional_analysis["Profit Margin %"] = (
    regional_analysis["Profit"] / regional_analysis["Sales"] * 100
)

regional_analysis = regional_analysis.sort_values(
    "Sales", ascending=False
)

print(regional_analysis.to_string(index=False))

print("\n===== CATEGORY PERFORMANCE =====")

category_analysis = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

category_analysis["Profit Margin %"] = (
    category_analysis["Profit"] / category_analysis["Sales"] * 100
)

category_analysis = category_analysis.sort_values(
    "Sales", ascending=False
)

print(category_analysis.to_string(index=False))

print("\n===== SUB-CATEGORY PERFORMANCE =====")

subcategory_analysis = df.groupby("Sub-Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

subcategory_analysis["Profit Margin %"] = (
    subcategory_analysis["Profit"] / subcategory_analysis["Sales"] * 100
)

subcategory_analysis = subcategory_analysis.sort_values(
    "Profit", ascending=True
)

print(subcategory_analysis.to_string(index=False))

print("\n===== DISCOUNT vs PROFITABILITY =====")

discount_analysis = df.groupby("Discount").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

discount_analysis["Profit Margin %"] = (
    discount_analysis["Profit"] / discount_analysis["Sales"] * 100
)

print(discount_analysis.to_string(index=False))

print("\n===== FURNITURE DISCOUNT ANALYSIS =====")

furniture_discount = df[df["Category"] == "Furniture"].groupby("Discount").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

furniture_discount["Profit Margin %"] = (
    furniture_discount["Profit"] / furniture_discount["Sales"] * 100
)

print(furniture_discount.to_string(index=False))

print("\n===== FURNITURE SUB-CATEGORY vs DISCOUNT =====")

furniture_subcategory = df[df["Category"] == "Furniture"].groupby(
    ["Sub-Category", "Discount"]
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

furniture_subcategory["Profit Margin %"] = (
    furniture_subcategory["Profit"] /
    furniture_subcategory["Sales"] * 100
)

print(furniture_subcategory.to_string(index=False))

print("\n===== LOSS-MAKING PRODUCTS =====")

loss_products = df.groupby(
    ["Product ID", "Product Name", "Category", "Sub-Category"]
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

loss_products = loss_products[loss_products["Profit"] < 0]

loss_products = loss_products.sort_values(
    "Profit", ascending=True
)

print(loss_products.head(15).to_string(index=False))

print("\n===== CUSTOMER SEGMENT PERFORMANCE =====")

segment_analysis = df.groupby("Segment").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique"),
    Customers=("Customer ID", "nunique")
).reset_index()

segment_analysis["Profit Margin %"] = (
    segment_analysis["Profit"] / segment_analysis["Sales"] * 100
)

print(segment_analysis.to_string(index=False))

# ============================================================
# CUSTOMER-LEVEL PERFORMANCE
# ============================================================

print("\n===== CUSTOMER PERFORMANCE =====")

customer_analysis = df.groupby(
    ["Customer ID", "Customer Name"]
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique"),
    Quantity=("Quantity", "sum")
).reset_index()

customer_analysis["Profit Margin %"] = (
    customer_analysis["Profit"] /
    customer_analysis["Sales"] * 100
)

print("\n--- TOP CUSTOMERS BY SALES ---")
print(
    customer_analysis
    .sort_values("Sales", ascending=False)
    .head(15)
    .to_string(index=False)
)

print("\n--- LOSS-MAKING CUSTOMERS ---")
print(
    customer_analysis[customer_analysis["Profit"] < 0]
    .sort_values("Profit")
    .head(15)
    .to_string(index=False)
)


# ============================================================
# STATE PERFORMANCE
# ============================================================

print("\n===== STATE PERFORMANCE =====")

state_analysis = df.groupby("State").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

state_analysis["Profit Margin %"] = (
    state_analysis["Profit"] /
    state_analysis["Sales"] * 100
)

print("\n--- TOP 10 STATES BY SALES ---")
print(
    state_analysis
    .sort_values("Sales", ascending=False)
    .head(10)
    .to_string(index=False)
)

print("\n--- BOTTOM 10 STATES BY PROFIT ---")
print(
    state_analysis
    .sort_values("Profit")
    .head(10)
    .to_string(index=False)
)


# ============================================================
# CITY PERFORMANCE
# ============================================================

print("\n===== CITY PERFORMANCE =====")

city_analysis = df.groupby("City").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

city_analysis["Profit Margin %"] = (
    city_analysis["Profit"] /
    city_analysis["Sales"] * 100
)

print("\n--- TOP 10 CITIES BY SALES ---")
print(
    city_analysis
    .sort_values("Sales", ascending=False)
    .head(10)
    .to_string(index=False)
)

print("\n--- BOTTOM 10 CITIES BY PROFIT ---")
print(
    city_analysis
    .sort_values("Profit")
    .head(10)
    .to_string(index=False)
)


# ============================================================
# TOP & BOTTOM PRODUCTS
# ============================================================

print("\n===== PRODUCT PERFORMANCE =====")

product_analysis = df.groupby(
    ["Product ID", "Product Name", "Category", "Sub-Category"]
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

product_analysis["Profit Margin %"] = (
    product_analysis["Profit"] /
    product_analysis["Sales"] * 100
)

print("\n--- TOP 10 PRODUCTS BY SALES ---")
print(
    product_analysis
    .sort_values("Sales", ascending=False)
    .head(10)
    .to_string(index=False)
)

print("\n--- TOP 10 PRODUCTS BY PROFIT ---")
print(
    product_analysis
    .sort_values("Profit", ascending=False)
    .head(10)
    .to_string(index=False)
)

print("\n--- BOTTOM 10 PRODUCTS BY PROFIT ---")
print(
    product_analysis
    .sort_values("Profit")
    .head(10)
    .to_string(index=False)
)


# ============================================================
# YEARLY PERFORMANCE
# ============================================================

print("\n===== YEARLY PERFORMANCE =====")

df["Year"] = df["Order Date"].dt.year

yearly_analysis = df.groupby("Year").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique"),
    Customers=("Customer ID", "nunique")
).reset_index()

yearly_analysis["Profit Margin %"] = (
    yearly_analysis["Profit"] /
    yearly_analysis["Sales"] * 100
)

print(yearly_analysis.to_string(index=False))


# ============================================================
# YEAR-OVER-YEAR GROWTH
# ============================================================

print("\n===== YEAR-OVER-YEAR GROWTH =====")

yearly_analysis["Sales Growth %"] = (
    yearly_analysis["Sales"].pct_change() * 100
)

yearly_analysis["Profit Growth %"] = (
    yearly_analysis["Profit"].pct_change() * 100
)

print(
    yearly_analysis[
        [
            "Year",
            "Sales",
            "Profit",
            "Sales Growth %",
            "Profit Growth %"
        ]
    ].to_string(index=False)
)


# ============================================================
# MONTHLY PERFORMANCE
# ============================================================

print("\n===== MONTHLY PERFORMANCE =====")

df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.strftime("%B")

monthly_analysis = df.groupby(
    ["Year", "Month", "Month Name"]
).agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

monthly_analysis["Profit Margin %"] = (
    monthly_analysis["Profit"] /
    monthly_analysis["Sales"] * 100
)

print(monthly_analysis.to_string(index=False))


# ============================================================
# SHIP MODE PERFORMANCE
# ============================================================

print("\n===== SHIP MODE PERFORMANCE =====")

ship_mode_analysis = df.groupby("Ship Mode").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).reset_index()

ship_mode_analysis["Profit Margin %"] = (
    ship_mode_analysis["Profit"] /
    ship_mode_analysis["Sales"] * 100
)

print(ship_mode_analysis.to_string(index=False))


# ============================================================
# FINAL BUSINESS SUMMARY
# ============================================================

print("\n===== FINAL BUSINESS SUMMARY =====")

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Overall Profit Margin: {profit_margin:.2f}%")

print(
    "\nLowest Margin Region:",
    regional_analysis.loc[
        regional_analysis["Profit Margin %"].idxmin(),
        "Region"
    ]
)

print(
    "Lowest Margin Category:",
    category_analysis.loc[
        category_analysis["Profit Margin %"].idxmin(),
        "Category"
    ]
)

print(
    "Lowest Margin Sub-Category:",
    subcategory_analysis.loc[
        subcategory_analysis["Profit Margin %"].idxmin(),
        "Sub-Category"
    ]
)

print(
    "Highest Sales Customer:",
    customer_analysis.loc[
        customer_analysis["Sales"].idxmax(),
        "Customer Name"
    ]
)

print(
    "Highest Sales Product:",
    product_analysis.loc[
        product_analysis["Sales"].idxmax(),
        "Product Name"
    ]
)