from .models import Appraisal
from rest_framework import serializers

#serialization is the process of converting a Model to JSON. 
#Using a serializer, we can specify what fields should be present in the JSON representation of the model.


class AppraisalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appraisal
        fields = ['appraisal_ID', 'objective', 'review_year', 'department_ID','employee_ID','rating']
