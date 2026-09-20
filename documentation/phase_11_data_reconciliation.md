# Phase 11: Data Reconciliation (Raw → Python → SQL)

## Objective

The purpose of this phase was to prove that critical business totals remained consistent throughout the data pipeline:

Raw Data → Python Preparation → Azure SQL Database → Power BI

Power BI validation will be completed in Phase 26 after dashboard development.

---

## Reconciliation Metrics

The following metrics were validated:

- Total Orders
- Delivered Orders
- Cancelled Orders
- Order Items
- Customers
- Merchandise Value
- Freight Value
- Payment Value

---

## Validation Process

### Raw Layer

Original Olist CSV datasets were checked for record counts and business totals.

### Python Layer

Prepared datasets generated through Python scripts were validated.

Output:

`reconciliation/python_reconciliation.csv`

### SQL Layer

Azure SQL staging and warehouse tables were validated using SQL aggregation queries.

Results were compared against Python outputs.

Output:

`reconciliation/phase_11_reconciliation.csv`

---

## Result

All validated metrics matched between:

Raw Data ✅  
Python Prepared Data ✅  
Azure SQL Database ✅  

No unexplained differences were found.

Power BI validation is intentionally left pending until Phase 26.

---

## Conclusion

The data pipeline preserves data accuracy from ingestion through SQL warehouse loading, providing confidence before analytics development.