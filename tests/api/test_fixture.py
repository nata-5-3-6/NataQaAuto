import pytest

@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Nata'

@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == 'Akhremenko'
