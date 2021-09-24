import datetime

from elloadmin import settings

import jwt
from admin.clients.models import Clients


def new_token(data):
    refresh_Token = jwt.encode(
        {
            **data,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=settings.REFRESH_TOKEN_EXP_TIME),
            'iat': datetime.datetime.utcnow()
        },
        settings.REFRESH_SECRET, settings.JWT_ALGORITHM)

    access_token = jwt.encode(
        {
            **data,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXP_TIME),
            'iat': datetime.datetime.utcnow()
        },
        settings.ACCESS_SECRET, settings.JWT_ALGORITHM)
    return {"refresh_Token": refresh_Token, "access_token": access_token}


def validate_token(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    if token:
        try:
            data = jwt.decode(token, settings.ACCESS_SECRET,
                              settings.JWT_ALGORITHM)
            cuts = Clients.objects.filter(username=data.get("username"))
            if cuts.exists():
                return True, cuts[0]
            raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return False, "Token expired."
        except jwt.InvalidTokenError:
            return False, "Invalid Token"
        except Exception as e:
            return False, str(e)
    return False, "token is not provided."


# for forget password
def encode_data(user_id, base_url, expire=True):
    if expire == True:
        payload = {
            'uid': user_id,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(seconds=settings.EMAIL_TOKEN_EXP_TIME)
        }
    else:
        payload = {
            'uid': user_id,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(days=90)
        }
    encoded_data = jwt.encode(
        payload, settings.ACCESS_SECRET, settings.JWT_ALGORITHM)
    data = str(encoded_data)
    url = base_url+data
    return url


def decode_data(token):
    try:
        decoded_data = jwt.decode(token, settings.ACCESS_SECRET, algorithms=[
                                  settings.JWT_ALGORITHM])
    except(jwt.DecodeError, jwt.ExpiredSignatureError):
        return None
    return decoded_data['uid']
