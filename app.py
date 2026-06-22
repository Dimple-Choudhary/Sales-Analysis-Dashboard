
import streamlit as st

from src.utils import *
from src.visualizations import *

st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Analysis Dashboard")

st.write(
    "This dashboard analyzes sales performance using Python, SQL, Pandas, SQLite and Streamlit."
)

# Sidebar Filter
df = get_dataframe()

st.sidebar.header("Filters")

selected_product = st.sidebar.selectbox(
    "Select Product",
    ["ALL"] + get_unique_products()
)

if selected_product != "ALL":
    filtered_df = df[df["Product"] == selected_product]
else:
    filtered_df = df

# KPIs
total_revenue = filtered_df["Revenue"].sum()
total_orders = len(filtered_df)

top_product = (
    filtered_df.groupby("Product")["Revenue"]
    .sum()
    .idxmax()
)

best_month = (
    filtered_df.groupby("Month")["Revenue"]
    .sum()
    .idxmax()
)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Revenue",
    f"₹{total_revenue:,}"
)

col2.metric(
    "📦 Total Orders",
    total_orders
)

col3.metric(
    "🏆 Top Product",
    top_product
)

col4.metric(
    "📅 Best Month",
    best_month
)

# Revenue by Product Chart
st.subheader("📈 Revenue by Product")

revenue_by_product = get_revenue_by_product(filtered_df)

fig = revenue_by_product_chart(revenue_by_product)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Monthly Revenue Trend
st.subheader("📉 Monthly Revenue Trend")

monthly_revenue = get_monthly_revenue(filtered_df)

fig = monthly_revenue_chart(monthly_revenue)

st.plotly_chart(
    fig,
    use_container_width=True
)


# Product Share Chart
st.subheader("🥧 Product Revenue Share")

fig = product_share_chart(revenue_by_product)

st.plotly_chart(
    fig,
    use_container_width=True
)


# Quantity Sold by Product
st.subheader("📦 Quantity Sold by Product")

quantity_by_product = get_quantity_by_product(filtered_df)

fig = quantity_by_product_chart(quantity_by_product)

st.plotly_chart(
    fig,
    use_container_width=True
)


# Top Products Table
st.subheader("🏆 Top 3 Products")

top_3_products = get_top_3_products(filtered_df)

st.dataframe(
    top_3_products,
    use_container_width=True
)

# Monthly Revenue Table
st.subheader("📅 Top 3 Months")

top_3_months = get_top_3_months(filtered_df)

st.dataframe(
    top_3_months,
    use_container_width=True
)

