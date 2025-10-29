class CustomerFilter(django_filters.FilterSet):
    "name", "email"

class Meta:
    "model = Customer", "class Meta"

class CustomerNode(DjangoObjectType):
     Meta.interfaces = (relay.Node,)

    all_customers = DjangoFilterConnectionField(...)