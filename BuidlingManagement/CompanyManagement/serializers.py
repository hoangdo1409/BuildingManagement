# from django.urls import path, include
# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company
from .models import Staff
from .models import Title
from .models import SalaryTemplate
from .models import Unit
from .models import SalaryPaper
from .models import WorkDay
from .models import SalaryPeriodDetails

# import Company class for example
# Serializers define the API representation.
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = [  
            'uuid',
            'name',
            'address',
            'floor_count',
            'member_count',
            'tax_code',
            # 'owners',
            'get_child_company',
            'parent_company',
            'contact',
            'period_type',
            'created_by',
            'updated_by',
            'updated_at',
            'created_at',   
        ]

    def get_request_user(self):
        if 'request' in self.context and hasattr(self.context['request'], "user"):
            request_user = self.context['request'].user 
        return request_user

    def create(self, validated_data):
        # trong request co user ko hay la duoc gui bang bot
        validated_data["created_by"] = self.get_request_user()
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data["updated_by"] = self.get_request_user()
        instance.name = validated_data.get('name', instance)
        return super().update(instance, validated_data)


# HyperlinkedModelSerializer được sử dụng để tạo endpoint
class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = [
            'uuid',
            'name',
            'address',
            'get_all_work_day_by_period',
            'get_all_salary_work_day_by_period',
            'get_all_salary_by_period',
            'tax_code',
            'company',  
            'salary_template',
            'unit',
            'title',
            'created_at',
            'updated_at',
        ]

class SalaryTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalaryTemplate
        fields = [
            'uuid',
            'name',
            'salary',
        ]

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = [
            'uuid',
            'name',
        ]

class TitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Title
        fields = [
            'uuid',
            'name',
        ]

class SalaryPaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalaryPaper
        fields = [
            'uuid',
            'name',
        ]


class WorkDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkDay
        fields = [
            'uuid',
            'name',
        ]
    
    def get_request_user(self):
        if 'request' in self.context and hasattr(self.context['request'], "user"):
            request_user = self.context['request'].user
        return request_user
    
    def create(self, validated_data):
        validated_data['create_by'] = self.get_request_user()
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.get_request_user()
        return super().update(instance, validated_data)
    
class SalaryPeriodDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalaryPeriodDetails
        fields = '__all__'

    def get_request_user(self):
        if 'request' in self.context and hasattr(self.context['request'], 'user'):
            request_user = self.context['request'].user
        return request_user
    
    def create(self, validated_data):
        validated_data['created_by'] = self.get_request_user()
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['updated_by'] = self.get_request_user()
        return super().update(instance, validated_data)