from .api_autogenerated import api

from ninja import ModelSchema
from . import models

class PolicySchema(ModelSchema):
    class Config:
        model = models.Policy
        model_fields = "__all__"


@api.post("/config/policy/")
def config_policy_create(request, policy: PolicySchema):
    return {}
