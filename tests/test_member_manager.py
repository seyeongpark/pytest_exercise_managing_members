# tests/test_member_manager.py

import pytest

# Test Add member(s)
def test_add_member(member_manager):
    assert member_manager.add_member("user1", "User Park", "user1@gmail.com") == True
    assert member_manager.add_member("user2", "User Lee", "user2@gmail.com") == True
        
def test_add_member_invalide(member_manager):
    with pytest.raises(ValueError):
        # NOT len(user_id) < 3
        member_manager.add_member("us", "User Park", "user1@gmail.com")
    with pytest.raises(ValueError):
        # NOT name or name.strip()
        member_manager.add_member("user1", " ", "user@gmail.com")
    with pytest.raises(ValueError):
        # NOT @ in email or . in email
        member_manager.add_member("user1", "User Park", "usergmailcom")
    with pytest.raises(ValueError):
        # NOT Same user_id exist
        member_manager.add_member("user1", "User Park", "user1@gmail.com")
        member_manager.add_member("user1", "User Park", "user1@gmail.com")

# Test Get member(s)
def test_get_member(manager_with_multiple_members):
    assert manager_with_multiple_members.get_member("user1")
    
def test_get_member_invalide(manager_with_multiple_members):
    # member_id is not exist
    with pytest.raises(KeyError):
        manager_with_multiple_members.get_member("user3") 

# Test Remove member(s)
# case 1) 0 member exist
def test_remove_member_empty(empty_manager):
    with pytest.raises(KeyError):
        empty_manager.remove_member("user1")       

# case 1) 1 member exist
def test_remove_member_one(manager_with_one_member):
    assert manager_with_one_member.remove_member("user1") == True
# case 1) 2 or more members exist 
def test_remove_member_multiple(manager_with_multiple_members):
    assert manager_with_multiple_members.remove_member("user1") == True
    assert manager_with_multiple_members.remove_member("user2") == True
