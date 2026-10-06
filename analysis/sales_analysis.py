import pandas as pd

# Đọc dữ liệu bán hàng
df = pd.read_csv("data/sales.csv")

# Tính doanh thu
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# Hiển thị 5 dòng đầu tiên
print(df.head())

# Tính tổng doanh thu
total_revenue = df["Revenue"].sum()

print("Total Revenue:", total_revenue)

# Doanh thu theo sản phẩm
revenue_by_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Product:")
print(revenue_by_product)

# Doanh thu theo tháng
df["Date"] = pd.to_datetime(df["Date"])

monthly_revenue = (
    df.groupby(df["Date"].dt.to_period("M"))["Revenue"]
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_revenue)

import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu bán hàng
df = pd.read_csv("data/sales.csv")

# Tính doanh thu
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# Hiển thị 5 dòng đầu tiên
print(df.head())

# Tính tổng doanh thu
total_revenue = df["Revenue"].sum()

print("Total Revenue:", total_revenue)

# Doanh thu theo sản phẩm
revenue_by_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Product:")
print(revenue_by_product)

# Doanh thu theo tháng
df["Date"] = pd.to_datetime(df["Date"])

monthly_revenue = (
    df.groupby(df["Date"].dt.to_period("M"))["Revenue"]
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_revenue)


# =========================
# CHART — MONTHLY REVENUE
# =========================

months = monthly_revenue.index.astype(str)
revenue = monthly_revenue.values

plt.figure(figsize=(10, 5))

plt.plot(
    months,
    revenue,
    marker="o",
    linewidth=2
)

plt.title("Monthly Revenue — 2026")
plt.xlabel("Month")
plt.ylabel("Revenue (VND)")

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "charts/monthly_revenue.png",
    dpi=300
)

plt.show()

# =========================
# CHART — REVENUE BY PRODUCT
# =========================

products = revenue_by_product.index
product_revenue = revenue_by_product.values

plt.figure(figsize=(10, 5))

plt.bar(
    products,
    product_revenue
)

plt.title("Revenue by Product — 2026")
plt.xlabel("Product")
plt.ylabel("Revenue (VND)")

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "charts/revenue_by_product.png",
    dpi=300
)

plt.show()

# =========================
# BEST-SELLING PRODUCTS
# =========================

quantity_by_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQuantity Sold by Product:")
print(quantity_by_product)

# =========================
# CHART — QUANTITY SOLD
# =========================

products = quantity_by_product.index
quantities = quantity_by_product.values

plt.figure(figsize=(10, 5))

plt.bar(
    products,
    quantities
)

plt.title("Quantity Sold by Product — 2026")
plt.xlabel("Product")
plt.ylabel("Quantity")

plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig(
    "charts/quantity_by_product.png",
    dpi=300
)

plt.show()