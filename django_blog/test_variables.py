import os
# from dotenv import load_dotenv
# load_dotenv()

# email_user1 = os.environ.get('EMAIL_HOST_USER')
# email_password1 = os.environ.get('EMAIL_HOST_PASSWORD')

email_user = os.environ.get('EMAIL_USER')
email_password = os.environ.get('EMAIL_PASS')

# email_user1 = os.getenv('EMAIL_HOST_USER')
# email_password1 = os.getenv('EMAIL_HOST_PASSWORD')

# email_user = os.getenv('EMAIL_USER')
# email_password = os.getenv('EMAIL_PASS')


print(email_user)
print(email_password)

print("##############")

# print(email_user1)
# print(email_password1)

DEBUG = False
print(DEBUG)



# what is in .bash_profile
# export EMAIL_HOST_USER = "coolbreezegf@gmail.com"
# export EMAIL_HOST_PASSWORD = "2Muchfun"