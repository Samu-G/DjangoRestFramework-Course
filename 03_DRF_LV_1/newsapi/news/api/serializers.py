from rest_framework import serializers
from news.models import Article
from django.utils.timesince import timesince
from datetime import datetime

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__"

    time_since_publication = serializers.SerializerMethodField()
    # preleva l'oggetto correlato e serializza il campo con nome e cognome
    # dell'autore correlato in ForegnKey
    author = serializers.StringRelatedField()

    def get_time_since_publication(self, obj):
        publication_date = obj.publication_date
        time_delta = timesince(publication_date, datetime.now())
        return time_delta

    def validate(self, data):
        """
        verifica che i dati siano validi
        """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Titolo e Descrizione non possono essere uguali")
        return data

    def validate_title(self, title):
        """
        verifica che il titolo sia lungo al massimo 90 caratteri
        """
        if len(title) > 90:
            raise serializers.ValidationError("Il titolo non può essere più lungo di 90 caratteri")
        return title
    

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         """
#         crea e restituisce una nuova istanza di Article
#         sulla base dei dati validati (validated_data)
#         """
#         print(validated_data)
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         aggiorna e restituisce l'istanza di Article AGGIORNATA
#         sulla base dei dati validati (validated_data)
#         """
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)

#         instance.save()

#         return instance

#     def validate(self, data):
#         """
#         verifica che i dati siano validi
#         """
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Titolo e Descrizione non possono essere uguali")
#         return data

#     def validate_title(self, title):
#         """
#         verifica che il titolo sia lungo al massimo 90 caratteri
#         """
#         if len(title) > 90:
#             raise serializers.ValidationError("Il titolo non può essere più lungo di 90 caratteri")
#         return title