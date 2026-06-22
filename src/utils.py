import pandas as pd

df = pd.read_csv("data/sales.csv")


def get_dataframe():
    return df.copy()


def get_unique_products():
    return list(df["Product"].unique())


def get_total_revenue():
    return df["Revenue"].sum()


def get_total_orders():
    return len(df)


def get_top_product():
    return (
        df.groupby("Product")["Revenue"]
        .sum()
        .idxmax()
    )


def get_best_month():
    return (
        df.groupby("Month")["Revenue"]
        .sum()
        .idxmax()
    )


def get_revenue_by_product(data=None):
    if data is None:
        data = df

    return (
        data.groupby("Product")["Revenue"]
        .sum()
    )


def get_monthly_revenue(data=None):
    if data is None:
        data = df

    return (
        data.groupby("Month")["Revenue"]
        .sum()
    )


def get_top_3_products(data=None):
    if data is None:
        data = df

    return (
        data.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )


def get_top_3_months(data=None):
    if data is None:
        data = df

    return (
        data.groupby("Month")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )


def get_quantity_by_product(data=None):
    if data is None:
        data = df

    return (
        data.groupby("Product")["Quantity"]
        .sum()
    )

