# Phase 01: Project Setup, Dataset and GitHub Repository

## 1. Phase Objective

The objective of this phase was to establish the foundation of the **E-Commerce Decision Intelligence Platform** project.

The project aims to convert raw operational e-commerce data into a reliable analytical solution that helps management understand:

* Sales performance
* Customer behaviour
* Product performance
* Seller performance
* Delivery performance
* Customer satisfaction
* Payment behaviour
* Freight impact
* Data quality
* Business risks and opportunities

The overall project workflow will follow:

```
Raw CSV Data
      ↓
Python / Pandas
      ↓
SQL Server
      ↓
Dimensional Data Model
      ↓
Power BI
      ↓
DAX
      ↓
Validation
      ↓
Business Insights
```

---

# 2. Project Structure Created

A master project repository was created with the required folder structure:

```
Ecommerce_Master_Capstone/

│
├── raw_data/
├── python/
├── sql/
├── profiling/
├── reconciliation/
├── validation/
├── diagrams/
├── documentation/
│
├── README.md
└── GitHub_Repository_Link.txt
```

## Purpose of Each Folder

### raw_data/

Stores original source datasets downloaded from Kaggle.

### python/

Contains Python and Pandas scripts used for data preparation, profiling, and transformation.

### sql/

Contains SQL Server database scripts, queries, loading scripts, and analysis queries.

### profiling/

Stores source data profiling outputs and reports.

### reconciliation/

Stores Raw → Python → SQL → Power BI reconciliation results.

### validation/

Stores validation documents and testing results.

### diagrams/

Stores ERD, architecture diagrams, and data model diagrams.

### documentation/

Stores phase documentation, decisions, explanations, and project notes.

---

# 3. Dataset Setup

The project uses:

**Brazilian E-Commerce Public Dataset by Olist**

Source:

```
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
```

The dataset was downloaded and placed inside:

```
raw_data/
```

---

# 4. Dataset Files Verified

The following 9 source CSV files were successfully downloaded and verified:

| File Name                             | Status    |
| ------------------------------------- | --------- |
| olist_customers_dataset.csv           | Completed |
| olist_geolocation_dataset.csv         | Completed |
| olist_order_items_dataset.csv         | Completed |
| olist_order_payments_dataset.csv      | Completed |
| olist_order_reviews_dataset.csv       | Completed |
| olist_orders_dataset.csv              | Completed |
| olist_products_dataset.csv            | Completed |
| olist_sellers_dataset.csv             | Completed |
| product_category_name_translation.csv | Completed |

---

# 5. Data Handling Decision

The original CSV files were kept unchanged.

No manual modification was performed on the source files.

All future cleaning, transformation, and preparation activities will be performed through reproducible Python/Pandas processes.

Reason:

* Preserve source integrity
* Maintain traceability
* Allow validation between raw and processed data
* Support reproducible analytics workflow

---

# 6. Core Tools Setup

The following tools were selected for the project:

| Tool       | Purpose                                     |
| ---------- | ------------------------------------------- |
| Python     | Data preparation and automation             |
| Pandas     | Data manipulation and analysis              |
| SQL Server | Analytical database layer                   |
| SQL        | Data loading and business analysis          |
| Power BI   | Dashboard and reporting                     |
| DAX        | Business calculations and time intelligence |
| Git/GitHub | Version control and project history         |

Additional libraries may be introduced later where they provide clear analytical value.

---

# 7. Git and GitHub Setup

A Git repository was initialized locally.

Repository:

```
Ecommerce_Master_Capstone
```

GitHub repository created:

```
https://github.com/samm4777/Ecommerce_Master_Capstone
```

The local project was connected with the remote GitHub repository.

---

# 8. Git Repository Tracking Decision

Because Git does not track empty folders, `.gitkeep` files were added inside empty project folders.

Example:

```
raw_data/.gitkeep
python/.gitkeep
sql/.gitkeep
documentation/.gitkeep
```

Purpose:

* Maintain required folder structure
* Allow repository structure to exist before files are generated
* Keep project organization consistent from the beginning

---

# 9. Files Produced During Phase 01

Created files:

```
README.md

GitHub_Repository_Link.txt

documentation/phase_01_project_setup.md
```

Dataset files added:

```
raw_data/

olist_customers_dataset.csv
olist_geolocation_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_order_reviews_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv
olist_sellers_dataset.csv
product_category_name_translation.csv
```

---

# 10. Key Decisions Made

## Decision 1:

Maintain original raw files without manual editing.

### Reason:

Ensures data integrity and allows future reconciliation.

---

## Decision 2:

Use a structured multi-folder project architecture.

### Reason:

Separates raw data, processing, analytics, validation, and documentation activities.

---

## Decision 3:

Use Git from the beginning.

### Reason:

Provides genuine development history and tracks project progress phase-by-phase.

---

# 11. Problems Faced and Solutions

| Problem                                              | Solution                                                 |
| ---------------------------------------------------- | -------------------------------------------------------- |
| Git does not track empty folders                     | Added `.gitkeep` files                                   |
| PowerShell mkdir syntax differed from Linux commands | Used PowerShell-compatible folder creation commands      |
| Need for repository structure before analysis starts | Created complete folder structure before adding datasets |

---

# 12. Phase 01 Completion Checklist

| Requirement                 | Status      |
| --------------------------- | ----------- |
| Project folder created      | ✅ Completed |
| Required folders created    | ✅ Completed |
| Olist dataset downloaded    | ✅ Completed |
| All 9 CSV files verified    | ✅ Completed |
| Raw files kept unchanged    | ✅ Completed |
| Core tools defined          | ✅ Completed |
| Git initialized             | ✅ Completed |
| GitHub repository created   | ✅ Completed |
| Repository link saved       | ✅ Completed |
| Phase documentation created | ✅ Completed |

---

# 13. Next Phase

The next phase will focus on:

**Phase 02 — Source Data Profiling**

Objectives:

* Profile all 9 datasets before transformation
* Understand dataset size, columns, data types, missing values, duplicates, identifiers, relationships, suspicious values, and data-quality concerns
* Produce summarized profiling outputs

