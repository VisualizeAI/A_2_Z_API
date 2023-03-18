from django.core.validators import RegexValidator
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

import datetime
import uuid
from storages.backends.s3boto3 import S3Boto3Storage

class MyUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, **extra_fields):
        """
        Create and save a User with the given email, fullname, and password.
        """
        if not email:
            raise ValueError(_('The user must have an email'))

        if not password:
            raise ValueError(_('The user must have a password'))

        if not first_name:
            raise ValueError(_('The user must have a full name'))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, password, first_name, **extra_fields):
        """
        Create and save a SuperUser with the given email, fullname, and password.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, first_name, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    '''
    password field supplied by AbstractBaseUser
    last_login field supplied by AbstractBaseUser
    is_superuser field provided by PermissionsMixin if we use PermissionsMixin
    groups field provided by PermissionsMixin if we use PermissionsMixin
    user_permissions field provided by PermissionsMixin if we use PermissionsMixin
    '''
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'mobile_number', 'gender', 'date_of_birth']   # while creating superuser from command it will ask these fields to enter value.
    EMAIL_FIELD = 'email'              # this is returned when we call get_email_field_name() method.
    
    # Field validators
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    # Fields
        # Visible fields
    UId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=21)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    mobile_number = models.CharField(max_length=17, unique=True, blank=False, null= False, validators=[mobile_regex], default=None)
    gender = models.CharField(max_length=7, blank=True, null=True, choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    date_of_birth = models.DateField(blank=False, null=False, default=datetime.date(1900,1,1))
    img = models.ImageField(blank=True, null=True, storage=S3Boto3Storage(bucket_name='project-a2z-api', region_name='us-east-1'), upload_to='User/Profiles')

        # Non-visible fields
    email_verified = models.BooleanField(verbose_name='Email Verified', default=False)
    mobile_verified = models.BooleanField(verbose_name='Mobile Verified', default=False)
    
    is_active = models.BooleanField(
        default=True,
        help_text='Designates whether this user should be treated as active.Unselect this instead of deleting accounts.',
    )
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.'
    )

    date_joined = models.DateTimeField(help_text='date joined', default=datetime.datetime.now())

    objects = MyUserManager()

    class Meta:
        ordering = ['-email',]

    def __str__(self):
        email = '%s' % (self.email)
        return email
    
    def get_full_name(self):
        return self.first_name.strip()+" "+self.last_name.strip()

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perm_list, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def email_user(self):pass

    def get_user_permissions(self):pass

    def get_group_permissions(self):pass

    def get_all_permissions(self):pass