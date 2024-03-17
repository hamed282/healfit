from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone_number, password):
        if not first_name:
            raise ValueError('First Name must be')
        if not last_name:
            raise ValueError('Last Name must be')
        if not email:
            raise ValueError('Email must be')
        if not phone_number:
            raise ValueError('Phone Number must be')

        user = self.model(first_name=first_name,
                          last_name=last_name,
                          email=self.normalize_email(email), phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, phone_number, password):
        user = self.create_user(first_name, last_name, email, phone_number, password)
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
