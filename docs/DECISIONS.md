# DECISIONS.md

## Why CSV for SAP?

CSV exports are common operational workflows in enterprise environments.

## Why REST APIs?

REST APIs simplify frontend/backend communication and prototype delivery.

## Assumptions

- Utility data arrives as CSV exports
- Fuel quantities are numeric
- One tenant exists for prototype scope

## Simplifications

- No real SAP integration
- No PDF OCR parsing
- No async ingestion jobs