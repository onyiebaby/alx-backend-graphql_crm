import graphene
from graphene_django import DjangoObjectType

from alx-backend-graphql_crm.crm.models import Category, crm

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "crm")

class crmType(DjangoObjectType):
    class Meta:
        model = crm
        fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType)
    crm = graphene.List(crmType)
    category  _by_name