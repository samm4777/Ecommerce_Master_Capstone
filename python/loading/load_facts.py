"""
Phase 10:
Load Fact Tables into Azure SQL Database

FactOrders:
One row = one customer order

FactOrderItems:
One row = one product item belonging to one order

FactPayments:
One row = one payment transaction

FactReviews:
One row = one customer review
"""


from sqlalchemy import text
from python.config.database_config import get_engine



# =====================================================
# FACT ORDERS
# =====================================================

def load_orders():

    engine = get_engine()

    query = """

    TRUNCATE TABLE fact.Orders;


    INSERT INTO fact.Orders
    (
        order_id,
        customer_key,
        date_key,
        geography_key,
        order_status,
        delivery_days
    )


    SELECT

        o.order_id,

        c.customer_key,

        d.date_key,

        g.geography_key,

        o.order_status,


        DATEDIFF(
            DAY,
            TRY_CONVERT(datetime,o.order_purchase_timestamp),
            TRY_CONVERT(datetime,o.order_delivered_customer_date)
        )


    FROM stg.orders o


    LEFT JOIN stg.customers sc

        ON o.customer_id = sc.customer_id



    LEFT JOIN
    (
        SELECT
            customer_unique_id,
            MIN(customer_key) AS customer_key

        FROM dim.Customer

        GROUP BY customer_unique_id

    ) c

        ON sc.customer_unique_id = c.customer_unique_id



    LEFT JOIN dim.Date d

        ON CONVERT(
            INT,
            FORMAT(
                TRY_CONVERT(datetime,o.order_purchase_timestamp),
                'yyyyMMdd'
            )
        ) = d.date_key



    LEFT JOIN
    (
        SELECT

            geolocation_zip_code_prefix,

            MIN(geography_key) AS geography_key


        FROM dim.Geography

        GROUP BY geolocation_zip_code_prefix

    ) g

        ON sc.customer_zip_code_prefix =
           g.geolocation_zip_code_prefix;



    """

    with engine.begin() as conn:
        conn.execute(text(query))


    print("FactOrders loaded")





# =====================================================
# FACT ORDER ITEMS
# =====================================================


def load_order_items():

    engine = get_engine()


    query = """

    TRUNCATE TABLE fact.OrderItems;


    INSERT INTO fact.OrderItems
    (
        order_id,
        product_key,
        seller_key,
        price,
        freight_value
    )


    SELECT


        oi.order_id,

        p.product_key,

        s.seller_key,

        oi.price,

        oi.freight_value



    FROM stg.order_items oi



    LEFT JOIN dim.Product p

        ON oi.product_id = p.product_id



    LEFT JOIN dim.Seller s

        ON oi.seller_id = s.seller_id;



    """

    with engine.begin() as conn:
        conn.execute(text(query))


    print("FactOrderItems loaded")






# =====================================================
# FACT PAYMENTS
# =====================================================


def load_payments():

    engine = get_engine()


    query = """

    TRUNCATE TABLE fact.Payments;


    INSERT INTO fact.Payments
    (
        order_id,
        payment_sequential,
        payment_type,
        payment_value
    )


    SELECT

        order_id,

        payment_sequential,

        payment_type,

        payment_value


    FROM stg.payments;



    """

    with engine.begin() as conn:
        conn.execute(text(query))


    print("FactPayments loaded")






# =====================================================
# FACT REVIEWS
# =====================================================


def load_reviews():

    engine = get_engine()


    query = """

    TRUNCATE TABLE fact.Reviews;


    INSERT INTO fact.Reviews
    (
        order_id,
        review_score
    )


    SELECT

        order_id,

        review_score


    FROM stg.reviews;



    """

    with engine.begin() as conn:
        conn.execute(text(query))


    print("FactReviews loaded")






# =====================================================
# MAIN
# =====================================================


def load_facts():

    print("Loading facts...")


    load_orders()

    load_order_items()

    load_payments()

    load_reviews()


    print("All facts loaded successfully")




if __name__ == "__main__":

    load_facts()