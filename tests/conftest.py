# tests/conftest.py

import pytest
from apps.member_manager import MemberManager

@pytest.fixture
def member_manager():
    return MemberManager()

@pytest.fixture
def empty_manager():
    # 0 member exist
    manager = MemberManager()
    return manager

@pytest.fixture
def manager_with_one_member():
    # 1 member exist
    manager = MemberManager()
    manager.add_member("user1", "User Park", "user1@gmail.com")
    
    return manager

@pytest.fixture
def manager_with_multiple_members():
    # 2 or more members exist
    manager = MemberManager()
    manager.add_member("user1", "User Park", "user1@gmail.com")
    manager.add_member("user2", "User Lee", "user2@gmail.com")
    
    return manager