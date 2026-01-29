"""
Koushik Module - User Management Features
This module handles user authentication and management.
"""

class UserManager:
    """Class to manage user operations"""
    
    def __init__(self):
        self.users = {}
        print("UserManager initialized by Koushik")
    
    def add_user(self, username, email):
        """Add a new user to the system"""
        if username not in self.users:
            self.users[username] = {
                'email': email,
                'active': True
            }
            print(f"User {username} added successfully")
            return True
        else:
            print(f"User {username} already exists")
            return False
    
    def get_user(self, username):
        """Retrieve user information"""
        return self.users.get(username, None)
    
    def list_users(self):
        """List all users"""
        print("\nUser List:")
        print("-" * 40)
        for username, info in self.users.items():
            print(f"Username: {username}, Email: {info['email']}, Active: {info['active']}")
        print("-" * 40)
        return self.users

def authenticate_user(user_manager, username, password):
    """
    Authenticate user credentials
    
    Note: This is a simplified educational implementation.
    In production, use proper password hashing and secure authentication.
    """
    print(f"Authenticating user: {username}")
    
    # Check if user exists in the system
    user = user_manager.get_user(username)
    if not user:
        print("Authentication failed: User not found!")
        return False
    
    # Simplified password check (In production: use bcrypt/hashing)
    if password and len(password) >= 6:  # Basic password validation
        print("Authentication successful!")
        return True
    
    print("Authentication failed: Invalid password!")
    return False

if __name__ == "__main__":
    print("Koushik Module - User Management System")
    print("=" * 50)
    
    # Demo usage
    manager = UserManager()
    manager.add_user("koushik", "koushik@example.com")
    manager.add_user("admin", "admin@example.com")
    manager.list_users()
    
    # Authenticate registered user
    print("\nTesting authentication:")
    authenticate_user(manager, "koushik", "password123")
    authenticate_user(manager, "nonexistent", "password123")
    authenticate_user(manager, "admin", "short")
