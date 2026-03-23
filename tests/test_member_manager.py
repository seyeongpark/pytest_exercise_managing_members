import pytest

# 회원 추가 테스트
def test_add_member(member_manager):
    # 추가한 회원 수를 카운트하여 검증
    count_before = member_manager.count_members()
    
    assert member_manager.add_member("user1", "User Park", "user1@gmail.com") == True
    assert member_manager.add_member("user2", "User Lee", "user2@gmail.com") == True
    # 회원 추가 후 총 인원 수는 2명이어야 함
    assert member_manager.count_members() == count_before + 2

def test_add_member_invalide(member_manager):
    with pytest.raises(ValueError):
        # user_id 길이가 3 미만인 경우
        member_manager.add_member("us", "User Park", "user1@gmail.com")     
    with pytest.raises(ValueError):
        # 이름이 비어있거나 공백인 경우
        member_manager.add_member("user1", " ", "user@gmail.com")
    with pytest.raises(ValueError):
        # 이메일 형식이 잘못된 경우
        member_manager.add_member("user1", "User Park", "usergmailcom")
    with pytest.raises(ValueError):
        # 동일한 user_id가 이미 존재하는 경우
        member_manager.add_member("user1", "User Park", "user1@gmail.com")
        member_manager.add_member("user1", "User Park", "user1@gmail.com")

def test_add_member_boundary(member_manager):
    # user_id 최소 허용 길이(3) 테스트
    assert member_manager.add_member("usr", "User", "user1@gmail.com") == True

def test_add_member_duplicate(member_manager):
    member_manager.add_member("user1", "User Park", "user1@gmail.com")
    
    with pytest.raises(ValueError):
        # 중복 user_id 추가 시 예외 발생
        member_manager.add_member("user1", "User Park", "user1@gmai.com")
        
    # 중복 추가 실패 후에도 회원 수는 1명 유지
    assert member_manager.count_members() == 1

# 파라미터화된 테스트 케이스
cases = [
    ("user1", "", "user1@gmail.com"),
    ("user2", " ", "user2@gmail.com"),
    ("user3", "User Kim", "user3gmail.com")
]
@pytest.mark.parametrize("user_id, name, email", cases)
def test_add_member_invalid_parametrize(empty_manager, user_id, name, email):
    with pytest.raises(ValueError):
        empty_manager.add_member(user_id, name, email)

# 회원 조회 테스트
def test_get_member(manager_with_multiple_members):
    assert manager_with_multiple_members.get_member("user1")

def test_get_member_invalide(manager_with_multiple_members):
    # 존재하지 않는 회원 조회 시 예외 발생
    with pytest.raises(KeyError) as info:
        manager_with_multiple_members.get_member("user3")

    assert str(info.value) == "'member not found'"
            
# 회원 데이터 검증
def test_get_member_data(manager_with_one_member):
    manager_data = manager_with_one_member.get_member("user1")
    assert manager_data["name"] == "User Park"
    assert manager_data["email"] == "user1@gmail.com"

# 회원 삭제 테스트
# case 1) 회원이 0명인 경우
def test_remove_member_empty(empty_manager):
    with pytest.raises(KeyError) as exc:
        empty_manager.remove_member("user1")       
    assert exc.value.args[0] == "member not found"
    
    # 삭제 후에도 회원 수는 0명 유지
    assert empty_manager.count_members() == 0

# case 2) 회원이 1명인 경우
def test_remove_member_one(manager_with_one_member):
    assert manager_with_one_member.remove_member("user1") == True
    # 삭제 후 회원 수는 0명
    assert manager_with_one_member.count_members() == 0
    
# case 3) 회원이 2명 이상인 경우
def test_remove_member_multiple(manager_with_multiple_members):
    assert manager_with_multiple_members.remove_member("user1") == True
    assert manager_with_multiple_members.remove_member("user2") == True
    # 삭제 후 회원 수는 0명
    assert manager_with_multiple_members.count_members() == 0
    
def test_remove_member_then_get_member(manager_with_one_member):
    assert manager_with_one_member.remove_member("user1") == True
    # 삭제된 회원 조회 시 예외 발생
    with pytest.raises(KeyError):
        manager_with_one_member.get_member("user1")
    # 삭제 후 회원 수는 0명
    assert manager_with_one_member.count_members() == 0
    
def test_member_flow(member_manager):
    # 회원 추가
    member_manager.add_member("user1", "User Park", "user1@gmail.com")
    member_manager.add_member("user2", "User Lee", "user2@gmail.com")
        
    # 회원 삭제
    member_manager.remove_member("user1")

    # 전체 흐름 검증
    assert member_manager.count_members() == 1
    assert member_manager.get_member("user2")["name"] == "User Lee"