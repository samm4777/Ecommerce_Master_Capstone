# Phase 16: Payment, Freight & Geographic Analysis

## Overview

This phase analyzes customer payment behaviour, freight cost patterns, and geographic business performance using SQL Server data warehouse tables.

The objective was to identify meaningful business patterns rather than only reporting transaction counts.

---

# 1. Payment Analysis

## Payment Methods Analysis

Payment methods were analyzed using:

- Payment type
- Number of orders
- Total payment value
- Average payment value per order


## Key Findings

Credit card was the dominant payment method by both transaction volume and total payment value.

Payment distribution showed:

- Credit card:
  - Highest number of orders
  - Highest total payment contribution

- Boleto:
  - Second major payment method
  - Significant contribution to total payment value

- Voucher and debit card:
  - Smaller contribution compared with major payment methods


## Installment Behaviour

Payment installments were analyzed to understand customer purchasing behaviour.

Metrics analyzed:

- Number of installments
- Order count
- Payment value
- Average order value


Findings:

Customers using installments showed different purchasing patterns compared with single-payment customers.

Higher installment counts were associated with larger average order values, indicating installment options supported higher-value purchases.


---

# 2. Freight Analysis

## Freight Cost Framework

Freight performance was evaluated using:

- Total merchandise value
- Total freight value
- Freight percentage of product value


Formula:
