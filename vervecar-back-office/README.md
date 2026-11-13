# VerveCar Back Office

Production back-office web application for VerveCar, a Bangkok dealership that imports new Daihatsu Hijet Cargo vans from Japan.

| | |
|---|---|
| **Client** | VerveCar, Bangkok (real business) |
| **Date** | September – October 2026 |
| **Team** | 2 members |
| **My role** | Requirements, proof of concept and most of the application |

> The source code belongs to the client and is not published. All screenshots use demonstration data. The interface is in Thai.

## Overview

Before this application, stock checks, sales records and customer documents depended on phone calls, LINE messages and paper forms, and the managing director had to answer stock questions throughout the day. The application brings stock, sales, documents and customer follow-up into one system available on desktop and mobile.

## My contribution

- Gathered and defined the requirements with the managing director, and built the first proof of concept.
- Built most of the application, including the stock board, the sales workflow, document generation, the finance calculator, reminders and data export.
- Worked on the database schema and the access rules that restrict cost and profit information to the managing director.

## Features

- **Stock management:** every vehicle with its status (available, booked, awaiting finance, sold), time in stock, search and filters; vehicles in stock for more than three months are flagged automatically.
- **Sales workflow:** sales staff record a sale and the managing director reviews it. A sale is approved automatically once the vehicle and commission are complete, and a checklist shows any missing information.
- **Finance calculator:** down payment as a percentage or an amount, 48/60/72-month instalments from editable bank rate tables (VAT included), and a ready-to-send LINE message for the customer.
- **Documents:** quotation PDF and printable booking form.
- **Customer follow-up:** leads rated Hot or Cool, with a private conversation between the managing director and the salesperson for each lead.
- **Alerts and audit history:** reminders for vehicles awaiting registration and for insurance renewals, and a complete history of status changes.
- **Access control and export:** cost and profit visible to the managing director only; CSV/JSON export with or without cost data.

## Results (estimates by the managing director)

| Task | Before | After |
|---|---|---|
| Preparing a quotation | ~20 min | ~5 min |
| Preparing a booking form | ~10 min | ~5 min |
| Checking stock availability | Phone call to the managing director | Immediate, in the app |
| Finding a past sale | ~10 min in paper files | Under 1 min |

## Screenshots

| | |
|---|---|
| ![](screenshots/01_home_dashboard_alerts.png) | ![](screenshots/03_stock_list_with_cost_MD_view.png) |
| ![](screenshots/00_finance_calculator.png) | ![](screenshots/05_followup_private_chat_MD_sales.png) |
| ![](screenshots/07_booking_form_print.png) | ![](screenshots/10_status_history_audit_log.png) |

Additional screenshots are available in [screenshots/](screenshots).

**Tech stack:** React, TypeScript, Vite (Progressive Web App), Supabase (PostgreSQL, Auth, Storage, Edge Functions), Cloudflare
