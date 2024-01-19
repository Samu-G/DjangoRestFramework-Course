from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly
from ebooks.api.pagination import SmallSetPagination

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by('id') # order_by('-id')
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user
        # limita ad una recensione per utente a libro
        review_queryset = Review.objects.filter(ebook=ebook, review_author=self.request.user)
        if review_queryset.exists():
            raise ValidationError("Hai gia' recensito questo libro!")
        else:
            serializer.save(ebook=ebook)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# class EbookListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     # *args e **kwargs consente di gestire un numero variabile di parametri!
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
