class CategoriesSerializer(serializers.ModelSerializer):
    meal = serializers.JSONField(default=None, read_only=True)

    class Meta:
        model = Categories
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['categoryJson'] = MainCategoriesSerializer(
            instance.category).data
        return response
def to_representation(self, instance):
        response = super().to_representation(instance)

        response['categoryJson'] = MainCategoriesSerializer(
            instance.category).data
        return response
#to_representation-da islan zadyny return edip bilyan