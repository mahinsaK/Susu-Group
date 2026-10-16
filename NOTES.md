# Assumptions

- Members are identified by unique names.
- Members can only be added before the first contribution is recorded.
- A susu cycle ends after every member has received the pot once.
- Contributions are recorded only for the current active week.
- Decimal is used for all monetary values.

# Design Decisions

- Payments are stored by week and then by member.
- Business logic is kept inside SusuGroup.
- CLI input/output is kept separate from business logic.

# Improvements With More Time

- Persistent storage using SQLite.
- Member IDs in addition to names.
- Better CLI formatting.
- Multiple susu groups.
- Exporting reports.