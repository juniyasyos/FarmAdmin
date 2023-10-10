class FinancialTransaction:
    def __init__(self, id, land_id, transaction_type, date, amount, description):
        self.id = id
        self.land_id = land_id
        self.transaction_type = transaction_type
        self.date = date
        self.amount = amount
        self.description = description