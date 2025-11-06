import graphene
from .models import Customer
from crm.models import Product
class Meta:
    model = Customer
    fields =  ("id", "name", "email", "phone")

class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)
 
class CRMQuery():
    hello = graphene.String(default_value='Hello, GraphQL!')



    "save()"

class Mutation(graphene.ObjectType):
    "CreateCustomer", "customer=customer"
    create_customer = CreateCustomer.Field()

class CustomerNode(DjangoObjectType):
    Meta.interfaces = (relay.Node,)

    all_customers = DjangoFilterConnectionField(...)

class UpdateLowStockProducts(graphene.Mutation):
    "UpdateLowStockProducts", "10"    