from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from posting.models import Posting
from posting.serializers import PostingSerializer
from posting.utils import check_password


class PostingViewSet(viewsets.ModelViewSet):
    """
    블로그 생성, 수정, 삭제, 리스트 조회 API
    """
    queryset = Posting.objects.all().order_by("-created_at")
    serializer_class = PostingSerializer

    def destroy(self, request, *args, **kwargs):
        """
        삭제하기 전 비밀번호 체크
        :param request: password
        :return:
        """
        try:
            password = request.data.get("password", None)
            posting_instance = Posting.objects.get(id=self.kwargs.get("pk"))

            if not password:
                raise ValidationError("password 값이 잘못되었습니다.")

            if not check_password(password, posting_instance):
                raise ValidationError("비밀번호가 맞지 않습니다.")

            return super(PostingViewSet, self).destroy(request, *args, **kwargs)

        except Posting.DoesNotExist as e:
            return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)
