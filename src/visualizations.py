
import plotly.express as px


def revenue_by_product_chart(revenue_by_product):
    fig = px.bar(
        x=revenue_by_product.index,
        y=revenue_by_product.values,
        title="Revenue by Product",
        labels={
            "x": "Product",
            "y": "Revenue"
        }
    )

    return fig


def monthly_revenue_chart(monthly_revenue):
    fig = px.line(
        x=monthly_revenue.index,
        y=monthly_revenue.values,
        title="Monthly Revenue Trend",
        labels={
            "x": "Month",
            "y": "Revenue"
        },
        markers=True
    )

    return fig


def product_share_chart(revenue_by_product):
    fig = px.pie(
        values=revenue_by_product.values,
        names=revenue_by_product.index,
        title="Product Revenue Share"
    )

    return fig


def quantity_by_product_chart(quantity_by_product):
    fig = px.bar(
        x=quantity_by_product.index,
        y=quantity_by_product.values,
        title="Quantity Sold by Product",
        labels={
            "x": "Product",
            "y": "Quantity"
        }
    )

    return fig

