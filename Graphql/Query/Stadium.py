from core.models import Stadium, Duration
from graphene import ObjectType, relay
from Graphql.QueryStructure import QueryFields
from rest_framework import status as status_code
from ..Relay import relays
import graphene


class AllStadiumByType(ObjectType, QueryFields):
    data = relay.ConnectionField(
        relays.StadiumConnection, type_id=graphene.ID(required=True))

    def resolve_data(root, info, **kwargs):
        print(kwargs)
        user = info.context.META['user']
        if not QueryFields.is_valide(info, user, 'core.view_stadium'):
            return QueryFields.rise_error(user)
        data = Stadium.objects.filter(
            type_id__id=kwargs['type_id'], is_deleted=False, is_available=True)
        if not data.exists():
            QueryFields.set_extra_data(
                user, status_code.HTTP_404_NOT_FOUND, 'not exists')
            return []
        QueryFields.set_extra_data(user, status_code.HTTP_200_OK, 'ok')
        return data


class GetStadium(ObjectType, QueryFields):
    data = relay.ConnectionField(
        relays.StadiumConnection, club_id=graphene.ID(required=True))

    def resolve_data(root, info, **kwargs):
        print(kwargs)
        user = info.context.META['user']
        if not QueryFields.is_valide(info, user, 'core.view_stadium'):
            return QueryFields.rise_error(user)
        data = Stadium.objects.filter(
            section_id__club_id__id=kwargs['club_id'], is_deleted=False, is_available=True)
        if not data.exists():
            QueryFields.set_extra_data(
                user, status_code.HTTP_404_NOT_FOUND, 'not exists')
            return []
        QueryFields.set_extra_data(user, status_code.HTTP_200_OK, 'ok')
        return data


class GetStadiumByType(ObjectType, QueryFields):
    data = relay.ConnectionField(
        relays.StadiumConnection, club_id=graphene.ID(required=True), type_id=graphene.ID(), size=graphene.Int())

    def resolve_data(root, info, **kwargs):
        print(kwargs)
        user = info.context.META['user']
        if not QueryFields.is_valide(info, user, 'core.view_stadium'):
            return QueryFields.rise_error(user)
        data = queryByFilter(kwargs)
        if not data.exists():
            QueryFields.set_extra_data(
                user, status_code.HTTP_404_NOT_FOUND, 'not exists')
            return []
        QueryFields.set_extra_data(user, status_code.HTTP_200_OK, 'ok')
        return data


def queryByFilter(kwargs: object) -> Stadium.objects.filter:
    if 'type_id' in kwargs and 'size' in kwargs:
        data = Stadium.objects.filter(
            size=kwargs['size'], type_id__id=kwargs['type_id'], section_id__club_id__id=kwargs['club_id'], is_deleted=False, is_available=True)
    elif 'type_id' in kwargs and not('size' in kwargs):
        data = Stadium.objects.filter(
            type_id__id=kwargs['type_id'], section_id__club_id__id=kwargs['club_id'], is_deleted=False, is_available=True)
    elif not('type_id' in kwargs) and 'size' in kwargs:
        data = Stadium.objects.filter(
            size=kwargs['size'], section_id__club_id__id=kwargs['club_id'], is_deleted=False, is_available=True)
    else:
        data = Stadium.objects.filter(
            section_id__club_id__id=kwargs['club_id'], is_deleted=False, is_available=True)
    return data