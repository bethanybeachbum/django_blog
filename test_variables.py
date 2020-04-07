import os

email_user = os.environ.get('EMAIL_HOST_USER')
email_password = os.environ.get('EMAIL_HOST_PASSWORD')

print(email_user)
print(email_password)



# export EMAIL_HOST_USER = 'coolbreezegf@gmail.com'
# export EMAIL_HOST_PASSWORD = '2Muchfun'