from decimal import Decimal

class SusuGroup:

    def __init__(self, weekly_amount):
        weekly_amount = Decimal(weekly_amount)
        if weekly_amount <= 0 :
            raise ValueError("weekly contribution must be grater than zero")

        self.weekly_amount = weekly_amount
        self.members = []

        self.current_week = 1

        self.payments = {}
        self.payout_history = []

    def add_member(self, member):
        if not member or not member.strip():
            raise ValueError("Member name cannot be empty")

        member = member.strip()

        if member in self.members:
            raise ValueError("Member already exists")

        self.members.append(member)

    def record_contribution(self, member, amount):
        member = member.strip()
        if not member in self.members:
                    raise ValueError("Enter valid Member name")

        amount = Decimal(amount)
        if amount <= 0:
             raise ValueError("Enter valid amount greater than zero")

        if self.current_week not in self.payments:
             self.payments[self.current_week] = {}

        week_payments = self.payments[self.current_week]
        already_paid = week_payments.get(member, Decimal("0.00"))
        amount_owed = self.amount_owed(member)

        if amount > amount_owed:
             raise ValueError("Payment is greater than the amount owed")

        week_payments[member] = already_paid + amount


    def amount_owed(self, member):
        if member not in self.members :
                    raise ValueError("Unknown member")

        week_payments = self.payments.get(self.current_week, {})
        already_paid = week_payments.get(member, Decimal("0.00"))
        return self.weekly_amount - already_paid

     




# add_member()
# record_contribution()
# close_week()
# get_report()