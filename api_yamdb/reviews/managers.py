from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, role='user',
                    **extra_fields):
        if username is None:
            raise TypeError('Пользователь должен иметь поле username')
        if email is None:
            raise TypeError('Пользователь должен иметь поле email')
        user = self.model(username=username, email=self.normalize_email(email),
                          role=role, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, role='admin',
                         **extra_fields):
        if password is None:
            raise TypeError('Суперпользователь должен иметь пароль')
        user = self.create_user(username, email, password, role=role,
                                **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user
