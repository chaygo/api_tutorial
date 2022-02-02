from rest_framework import serializers
from .models import Pictures, Section,Worker, Works


class WorkerSerializer(serializers.ModelSerializer):
    section = serializers.StringRelatedField(many=False)
    image_url=serializers.SerializerMethodField()
    class Meta:
        model = Worker
        fields = ['id','section','name','phone_number','email','adress','salary','years_of_experience','data_about_worker','image_url']

    def get_image_url(self, worker):
        request = self.context.get('request')
        image_url = worker.image.url
        return request.build_absolute_uri(image_url)
class PicturesSerializer(serializers.ModelSerializer):
    image_url=serializers.SerializerMethodField()
    class Meta:
        model=Pictures
        fields=['id','name','image_url']
    def get_image_url(self, picture):
        request = self.context.get('request')
        image_url = pictures.image.url
        return request.build_absolute_uri(image_url)
class WorksSerializer(serializers.ModelSerializer):
    section = serializers.StringRelatedField(many=False)
    image_url=serializers.SerializerMethodField()
    pictures = PicturesSerializer(many=True, read_only=True)
    class Meta:
        model=Works
        fields=['id','section','name','image_url','description','likes','views','pictures']

    def get_image_url(self, work):
        request = self.context.get('request')
        image_url = work.main_image.url
        return request.build_absolute_uri(image_url)
class SectionSerializer(serializers.ModelSerializer):
    workers = WorkerSerializer(many=True, read_only=True)
    works=WorksSerializer(many=True,read_only=True)
    class Meta:
        model = Section
        fields = ['id','name','number','short_description','created_at','updated_at','icons','workers','works']
