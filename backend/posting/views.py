from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posting.models import Posting
from posting.serializers import PostingSerializer


# 게시글 생성 및 게시글 리스트 조회
class PostingListCreateAPIView(APIView):
    def get(self, request):
        """
        게식시글 리스트 조회
        :param:
        :return: 게시글 리스트
        """
        queryset = Posting.objects.all()
        serializer = PostingSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        게시글 생성
        :param: title: str
        :param: content: str
        :param: password: str
        :return: 게시글 리스트
        """
        serializer = PostingSerializer(data=request.data)
        print("serializer: ", serializer)
        # print("data: ", serializer.data)
        serializer.is_valid(raise_exception=True)
        # password didn't hashing
        serializer.save()
        return Response(serializer.data)


class PostingDeleteUpdateAPIView(APIView):
    def delete(self, request, id):
        print("request : ", request.data, id)
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request):
        print("request : ", request.data)
        return Response({}, status=status.HTTP_200_OK)
