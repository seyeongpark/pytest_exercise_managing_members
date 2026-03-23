# apps/member_manager.py
class MemberManager:
    def __init__(self):
        self.members = {}

    def add_member(self, user_id, name, email):
        if not user_id or len(user_id) < 3:
            raise ValueError("user_id must be at least 3 characters long")

        if not name or not name.strip(): 
            raise ValueError("name cannot be empty")

        if "@" not in email or "." not in email:
            raise ValueError("invalid email format")

        if user_id in self.members:
            raise ValueError("user_id already exists")

        self.members[user_id] = {
            "name": name,
            "email": email,
        }
        return True

    def get_member(self, user_id):
        if user_id not in self.members:
            raise KeyError("member not found")
        return self.members[user_id]

    def remove_member(self, user_id):
        if user_id not in self.members:
            raise KeyError("member not found")
        del self.members[user_id]
        return True

    def count_members(self):
        return len(self.members)