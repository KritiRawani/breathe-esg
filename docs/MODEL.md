# MODEL.md

## Multi-Tenancy

Tenant model supports multiple enterprise clients in a shared platform architecture.

## RawRecord Design

RawRecord stores untouched source data for:
- auditability
- debugging
- reprocessing

## Audit Architecture

AuditLog tracks:
- status changes
- reviewer actions
- old/new values

## Scope Mapping

- Scope 1 → Fuel
- Scope 2 → Electricity
- Scope 3 → Travel

## Normalization Strategy

Data is normalized into consistent units before emissions calculation.