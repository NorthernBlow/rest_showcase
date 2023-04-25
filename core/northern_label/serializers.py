from rest_framework import serializers
from northern_label.models import Artists

class ArtistsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artists
		fields = ('name', 'description')