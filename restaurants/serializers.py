from rest_framework import serializers
from .models import Restaurant, Review, FavoriteRestaurant

class RestaurantSerializer(serializers.ModelSerializer):
    total_reviews = serializers.SerializerMethodField()
    is_open = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [
            'id', 'name', 'category', 'owner', 'rating', 'location', 'address', 'contact_number',
            'created_at', 'updated_at', 'total_reviews', 'opening_time', 'closing_time',
            'about', 'photo', 'is_open', 'latitude', 'longitude'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def get_total_reviews(self, obj):
        return obj.reviews.count()
    
    def get_is_open(self, obj):
        return obj.is_open()
    
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'restaurant', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'restaurant', 'created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value    

class FavoriteRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRestaurant
        fields = ['id', 'user', 'restaurant']
        read_only_fields = ['user']


class RestaurantStatisticsSerializer(serializers.ModelSerializer):
    favorite_count = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'favorite_count']

    def get_favorite_count(self, obj):
        return obj.favorites.count()
