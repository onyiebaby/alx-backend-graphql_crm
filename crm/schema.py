import graphene
from .models import Customer

class Meta:
    model = Customer
    fields =  ("id", "name", "email", "phone")

class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)
 
class CRMQuery():
    hello = graphene.String(default_value='Hello, GraphQL!')

