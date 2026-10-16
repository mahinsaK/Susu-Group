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
        pass

    def amount_owed(self, member):
        return self.weekly_amount - self.payments.get[member, Decimal("0.00")]




# add_member()
# record_contribution()
# close_week()
# get_report()