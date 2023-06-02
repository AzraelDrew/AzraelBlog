from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.hashers import check_password, make_password


class Password(ModelViewSet):
    def MakePassword(self, data):
        return make_password(data['password'], data['username'])

    def AuthPassword(self, data, password):
        return check_password(data['password'], password)
