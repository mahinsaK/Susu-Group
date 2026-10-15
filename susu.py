from decimal import Decimal

class SusuGroup:

    def __init__(self, weekly_amount):
        self.weekly_amount = Decimal(weekly_amount)
        self.members = []
        self.current_week = 1
        self.payments = {}
        self.payout_history = []

    def add_member(self, member):
        if member in self.members:
            raise ValueError("Member already exists")
        self.members.append(member)

    def record_contribution(member, amount):
            

# add_member()
# record_contribution()
# close_week()
# get_report()