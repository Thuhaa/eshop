from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class CustomUserManager(BaseUserManager):
	'''
	Custom user manager
	'''

	def create_user(self, email, password, first_name, last_name):
		'''
		This method creates and saves a user with the given email, password, firstname and lastname
		'''

		# Check if the email is provided. If not, raise an error
		if not email:
			raise ValueError('Users must have an email address')

		email = self.normalize_email(email)
		user = self.model(
			email=email, 
			first_name=first_name, 
			last_name=last_name,
			password=password)
		user.set_password(password)
		# save the user to the default database
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, first_name, last_name):
		'''
		Create a superuser with the given email, password, firstname, lastnama
		'''
		user = self.create_user(
			email=email, 
			password=password,
			first_name=first_name, 
			last_name=last_name
			)
		# Since the user is a superuser the following should be set
		user.is_active = True
		user.is_admin = True
		# save the superuser to the default database
		user.save(using=self._db)
		return user


class CustomUser(AbstractBaseUser):
	'''
	Custom user class inherits from the AbstractBaseUser. The fields email and password are required
	'''
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	

	# Specify the manager for this specific user model
	objects = CustomUserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self):
		return self.email

	# 
	class Meta:
		verbose_name = "Users"
		verbose_name_plural = "Users"

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True