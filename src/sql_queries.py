
import pandas as pd


def get_revenue_by_product_sql(conn):
    query = """
    SELECT Product,
    SUM(Revenue) AS Total_Revenue
    FROM sales
    GROUP BY Product
    """
    return pd.read_sql(query, conn)


def get_top_3_products_sql(conn):
    query = """
    SELECT Product,
    SUM(Revenue) AS Total_Revenue
    FROM sales
    GROUP BY Product
    ORDER BY Total_Revenue DESC
    LIMIT 3
    """
    return pd.read_sql(query, conn)


def get_monthly_revenue_sql(conn):
    query = """
    SELECT Month,
    SUM(Revenue) AS Monthly_Revenue
    FROM sales
    GROUP BY Month
    ORDER BY Monthly_Revenue DESC
    """
    return pd.read_sql(query, conn)


def get_best_month_sql(conn):
    query = """
    SELECT Month,
    SUM(Revenue) AS Monthly_Revenue
    FROM sales
    GROUP BY Month
    ORDER BY Monthly_Revenue DESC
    LIMIT 1
    """
    return pd.read_sql(query, conn)


def get_average_revenue_sql(conn):
    query = """
    SELECT AVG(Revenue) AS Average_Revenue
    FROM sales
    """
    return pd.read_sql(query, conn)


def get_total_revenue_sql(conn):
    query = """
    SELECT SUM(Revenue) AS Total_Revenue
    FROM sales
    """
    return pd.read_sql(query, conn)


def get_total_orders_sql(conn):
    query = """
    SELECT COUNT(OrderID) AS Total_Orders
    FROM sales
    """
    return pd.read_sql(query, conn)


def get_total_items_sold_sql(conn):
    query = """
    SELECT SUM(Quantity) AS Total_Items_Sold
    FROM sales
    """
    return pd.read_sql(query, conn)


def get_best_selling_product_sql(conn):
    query = """
    SELECT Product,
    SUM(Quantity) AS Total_Quantity
    FROM sales
    GROUP BY Product
    ORDER BY Total_Quantity DESC
    LIMIT 1
    """
    return pd.read_sql(query, conn)

