
# !!! This code is auto-generated, please do not modify
import json

from hashlib import sha1
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

from django.core import serializers
from django.contrib import admin
from django.utils.safestring import mark_safe


from . import models


class BaseGovstackAdmin(admin.ModelAdmin):
    readonly_fields = ('serialized_snapshot', 'serialized_hash',)

    def serialized_snapshot(self, instance):

        # Convert the data to sorted, indented JSON
        response = serializers.serialize('json', [instance, ], indent=2)
        
        # Strip the list
        json_dict = json.loads(response)
        response = json.dumps(json_dict[0]["fields"], indent=2)

        # Get the Pygments formatter
        formatter = HtmlFormatter(style='colorful')

        # Highlight the data
        response = highlight(response, JsonLexer(), formatter)

        # Get the stylesheet
        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        # Safe the output
        return mark_safe(style + response)

    serialized_snapshot.short_description = 'Object as JSON artifact'

    def serialized_hash(self, instance):
        # Convert the data to sorted, indented JSON
        response = serializers.serialize('json', [instance, ], indent=2)

        # Strip the list
        json_dict = json.loads(response)
        response = json.dumps(json_dict[0]["fields"], indent=2)

        hash_value = sha1(response.encode())
        return hash_value.hexdigest()

    serialized_hash.short_description = 'hash (SHA-1 of artifact)'


@admin.register(models.Individual)
class IndividualAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Agreement)
class AgreementAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AgreementData)
class AgreementDataAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Policy)
class PolicyAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.ConsentRecord)
class ConsentRecordAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Revision)
class RevisionAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Controller)
class ControllerAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Signature)
class SignatureAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AgreementPurpose)
class AgreementPurposeAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AgreementLifecycle)
class AgreementLifecycleAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.RegistryReference)
class RegistryReferenceAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AuditTracker)
class AuditTrackerAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AuditEventType)
class AuditEventTypeAdmin(BaseGovstackAdmin):
    pass



