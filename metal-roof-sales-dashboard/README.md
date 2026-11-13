# Metal-Roof Sales Dashboard

Browser-based sales analytics dashboard for PU MetalSheet, a metal-roofing company.

| | |
|---|---|
| **Context** | Class project with a real company; the CEO presented the brief and each student built an individual solution |
| **Date** | 2026 |
| **Team** | Individual version |
| **My role** | Design and development |

## Overview

The company's accounting software (Express) produces text-only sales reports that are difficult to read at a glance. This dashboard turns the exported CSV files into charts, breakdowns and a forecast. It is a single HTML file that runs entirely in the browser, so no installation is required and the data never leaves the user's computer.

## Features

- Automatic recognition of the three export types (cash sales, credit sales and deposits) on upload.
- Role-based views: executive, management and sales; each salesperson sees only their own figures.
- Monthly targets, month-on-month growth, product and customer breakdowns, and a demand-forecast page.
- English and Thai interface.

## Data and security

The company's data is confidential and is **not** included in this repository. The login is a demonstration of role-based views for this proof of concept and is not intended as a security mechanism.

## Try it

Open `MetalSheetDashboardPOC.html` in a browser, upload `sample_data/FAKE_demo_sales.csv` (490 fictitious invoices, March to August 2026) and sign in as `ceo` / `ceo123`.

## Screenshots (fictitious data)

| Executive overview | Sales trend |
|---|---|
| ![](screenshots/01_overview.png) | ![](screenshots/02_trend.png) |

| Products | Sales performance |
|---|---|
| ![](screenshots/03_products.png) | ![](screenshots/04_salespeople.png) |

**Tech stack:** HTML, CSS, JavaScript (no external dependencies)
