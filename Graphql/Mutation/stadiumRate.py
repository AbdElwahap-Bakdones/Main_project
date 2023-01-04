from ..ModelsGraphQL import typeobject, inputtype
import graphene
from core import models, serializer
from ..Auth.permission import checkPermission
from rest_framework import status as status_code
from .. import QueryStructure


class AddStadiumRate(graphene.Mutation, QueryStructure.Attributes):
    data = graphene.Field(typeobject.StadiumRateObjectType)

    class Arguments:
        StadiumRateData = inputtype.AddStadiumRateInput()

    @classmethod
    def mutate(self, root, info, **kwargs):
        try:
            user = info.context.META["user"]
            if not checkPermission("core.add_stadiumrate", user):
                return QueryStructure.MyReturn(self, None, 'You do not have permission to complete the process', status_code.HTTP_401_UNAUTHORIZED)
            seria = serializer.StadiumRateSerializer(
                data=kwargs["StadiumRateData"])
            if seria.is_valid():
                seria.validated_data
                msg = seria.errors
                status = status_code.HTTP_201_CREATED
                data = seria.save()
            else:
                msg = seria.errors
                data = None
                status = status_code.HTTP_406_NOT_ACCEPTABLE
        except Exception as e:
            msg = e
            data = None
            status = status_code.HTTP_500_INTERNAL_SERVER_ERROR
        return QueryStructure.MyReturn(instanse=self, data=data, message=msg, code=status)
