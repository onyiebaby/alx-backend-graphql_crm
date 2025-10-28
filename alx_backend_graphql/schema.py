import graphene
from graphene_django import DjangoObjectType
from alx-backend-graphql_crm.crm.models import Category, crm

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "email")

class Query(CRMQuery, graphene.ObjectType):
    all_customers = graphene.List(CustomerType)

    def resolve_all_customers(root, info):
        return Customer.objects.all()
    
schema = graphene.Schema(query=Query)    