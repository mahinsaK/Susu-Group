from decimal import Decimal
import pytest

from susu import SusuGroup

def test_partial_payment():
    group = SusuGroup("50.00")
    group.add_member("Ama")

    group.record_contribution("Ama", "30.00")

    assert group.amount_owed("Ama") == Decimal("20.00")

def test_week_cannot_close_when_member_owes():
    group = SusuGroup("50.00")

    group.add_member("Ama")
    group.add_member("Kofi")
    group.add_member("Esi")

    group.record_contribution("Ama", "50.00")
    group.record_contribution("Kofi", "50.00")
    group.record_contribution("Esi", "30.00")

    result = group.close_week()

    assert result["closed"] is False
    assert result["outstanding"]["Esi"] == Decimal("20.00")
    assert group.current_week == 1

# Group creation
def test_group_creation():
    group = SusuGroup("60.00")

    assert group is not None

# Duplicate member rejected
def test_duplicate_member_rejection():
    group = SusuGroup("50.00")
    
    group.add_member("Ama")
    with pytest.raises(ValueError):
        group.add_member("Ama")

# Unknown member rejected
def test_unknown_member_rejected():
    group = SusuGroup("50.00")
    group.add_member("Ama")

    with pytest.raises(ValueError, match="Enter valid Member name"):
        group.record_contribution("Kamal", "50.00")

# Negative payment rejected
def test_negative_payment_rejected():
    group = SusuGroup("50.00")
    group.add_member("Ama")

    with pytest.raises(ValueError, match="Enter valid amount greater than zero"):
        group.record_contribution("Ama", "-10.00")

# Zero payment rejected
def test_zero_payment_rejected():
    group = SusuGroup("50.00")
    group.add_member("Ama")

    with pytest.raises(ValueError, match="Enter valid amount greater than zero"):
        group.record_contribution("Ama", "0")

# Partial payment works
def test_partial_payment_works():
    group = SusuGroup("50.00")
    group.add_member("Ama")

    group.record_contribution("Ama", "20.00")

    assert group.amount_owed("Ama") == Decimal("30.00")

# Overpayment rejected
def test_overpayment_rejected():
    group = SusuGroup("50.00")
    group.add_member("Ama")

    with pytest.raises(ValueError, match="Payment is greater than the amount owed"):
        group.record_contribution("Ama", "60.00")

# Week cannot close
def test_week_cannot_close():
    group = SusuGroup("50.00")

    group.add_member("Ama")
    group.add_member("Nimal")

    group.record_contribution("Ama", "50.00")

    result = group.close_week()

    assert result["closed"] is False
    assert "Nimal" in result["outstanding"]

# Successful week closes
def test_successful_week_closes():
    group = SusuGroup("50.00")

    group.add_member("Ama")
    group.add_member("Nimal")

    group.record_contribution("Ama", "50.00")
    group.record_contribution("Nimal", "50.00")

    result = group.close_week()

    assert result["closed"] is True

# Correct payout recipient
def test_correct_payout_recipient():
    group = SusuGroup("50.00")

    group.add_member("Ama")
    group.add_member("Nimal")

    group.record_contribution("Ama", "50.00")
    group.record_contribution("Nimal", "50.00")

    result = group.close_week()

    assert result["payout"]["member"] == "Ama"

# Cannot add members after susu starts
def test_cannot_add_members_after_susu_starts():
    group = SusuGroup("50.00")

    group.add_member("Ama")

    group.record_contribution("Ama", "50.00")

    with pytest.raises(
        ValueError,
        match="Cannot add members after contributions have started"
    ):
        group.add_member("Nimal")        

