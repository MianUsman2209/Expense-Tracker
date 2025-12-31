# Wrapper for backward compatibility
from app.core.security import hash_password, verify_password

# Export with alternative names
get_password_hash = hash_password
verify_password_hash = verify_password
