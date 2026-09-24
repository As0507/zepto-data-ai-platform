# Data Pipeline

## Steps
1. Run `scrape_books.py` → scrapes ≥60 books, cleans data, converts GBP→INR, stores in SQLite.
2. Database file: `books.db` (auto-created).
3. Queries: see `queries.sql`.

## Design Decisions
- Fixed conversion rate: **1 GBP = 105.50 INR**.
- Schema: two tables (`categories`, `books`) with PK/FK.
- Median imputation or row drop for messy values.
