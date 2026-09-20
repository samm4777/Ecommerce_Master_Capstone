# Phase 07: Data Quality Report

## Objective

Identify the five most important data-quality issues found during source profiling and Python data preparation.

The issues are selected based on:
- Business impact
- Number of affected records
- Effect on analytical accuracy

---

# Data Quality Issues

| Issue | Number of Affected Records | Business Impact | Action Taken | Reason |
|---|---:|---|---|---|
| Missing order approval timestamps | 160 | Affects order lifecycle analysis and approval-time calculations | Retain / Investigate | Records are kept because removing orders would affect sales analysis. Missing values require further investigation. |
| Missing carrier handover timestamps | 1,783 | Impacts delivery performance calculations and carrier analysis | Retain | Missing values may represent incomplete delivery processes or cancelled orders. Removing them would reduce operational visibility. |
| Missing customer delivery timestamps | 2,965 | Affects on-time delivery, late delivery, and delivery delay calculations | Retain and Flag | Records are important for understanding order outcomes. Missing delivery dates need to be identified during delivery analysis. |
| Missing product category values | 610 | Affects product and category performance analysis | Replace | Missing categories were replaced with "Unknown" to preserve product records while maintaining category reporting completeness. |
| Duplicate geolocation records | Identified during profiling | May create duplication risk during geographic analysis | Investigate / Retain | Multiple geographic records can exist for the same location information. They require careful handling before analytical modeling. |

---

# Detailed Decisions

## 1. Missing Order Approval Timestamp

### Issue
Some orders do not contain approval timestamps.

### Impact
Approval-time analysis may be incomplete.

### Decision
Retain the records.

### Reason
Orders remain valid business records and should not be removed only because one timestamp is missing.

---

## 2. Missing Carrier Handover Timestamp

### Issue
Some orders do not have carrier delivery handover dates.

### Impact
Delivery performance analysis may be affected.

### Decision
Retain.

### Reason
The absence of a timestamp itself may represent a meaningful operational condition.

---

## 3. Missing Customer Delivery Timestamp

### Issue
Some orders do not contain final delivery dates.

### Impact
Cannot directly calculate delivery delay for those records.

### Decision
Retain and flag.

### Reason
Removing these records would hide potentially important operational cases.

---

## 4. Missing Product Categories

### Issue
Some products have no assigned category.

### Impact
Product category reporting becomes incomplete.

### Decision
Replace missing values with:
