from django.shortcuts import render
# import logging

# Create your views Here
# logging=logging.getlogger('auth')
# # register user
# from django.views import views
# from authentication.models import User
# from django.core.mail import EmailMessage
#
def home(request):
    return render(request, 'index.html')
#
# class UserRegistration(View):
#     def post(self,reqest,*args,**kwargs):
#         try:
#             pass
#             # get form data
#             email=request.POST['email']
#             logging.info(email)
#             password=request.POST['password']
#             logging.info(password)
#             #save user data
#             user=User(
#             email=email,
#             password=password
#             )
#             user.save()
#             # get user object
#             user=User.objects.get(email=email)
#             email_subject='ACTIVATE ACCOUNT'
#             email_body="""
#             Thank you for registering at Safari betting company,
#             Please activate your account here http://127.0.0.1:8000/?quetip={0}
#             """.format(str(user.id))
#             email = EmailMessage('ACTIVATE ACCOUNT', 'body', to=[email])
#             email.send()
#             #  send otp
#         except Exception as e:
#             raise e
#
# class EmailValidation(View):
#     def get (self,request,*args,**kwargs):
#         try:
#             '''
#             http://liz.co.ke/validate?id=user.id
#             Users.objects.get(ser_id-id).is_active=True.save(
#             )
#             '''
#         except Exception as e:
#             raise
#         else:
#             pass
#         finally:
#             pass

#
# class Placebet(self,request,*args,**kwargs):
#     try:
#         # form data
#
#         game_id=request.POST['game_id']
#         amount=request.POST['amount']
#         prediction=request.POST['prediction']

        # save user data
        # user=User(
        # game_id=game_id
        # amount=amount
        # prediction=prediction
        # )
            # send email bet placed
     #     '''
     # except Exception as e:
     #     raise
     # else:
     #     pass
     # finally:
     #     pass
