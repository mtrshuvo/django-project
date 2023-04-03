from django.contrib.auth.base_user import BaseUserManager

class UserManager (BaseUserManager) :
    use_in_migrations = True
    def create_user(self,email, password=None , **extra):
        if not email:
            raise ValueError ('Email is require')
        email = self.normalize_email (email)
        user = self.model (email = email,**extra)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra):
        
        extra.setdefault("is_staff", True)
        extra.setdefault("is_active", True)
        extra.setdefault("is_superuser", True)

        if extra.get("is_staff") is not True:
            raise ValueError("Must staf true")
        if extra.get("is_superuser") is not True:
            raise ValueError("Must is_superuser true")
        if extra.get("is_active") is not True:
            raise ValueError("Must is_active true")
        return self.create_user(email, password, **extra)

    