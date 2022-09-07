from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from posting.models import Posting
from posting.utils import hash_password, check_password


class PostingSerializer(serializers.ModelSerializer):
    """
    Posting Serialization
    """

    class Meta:
        model = Posting
        exclude = ["id"]
        extra_kwargs = {
            "password": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True}
        }

    def validate_password(self, password: str):
        """
        비밀번호 유효성 검사
            - 6자 이상
            - 숫자 1개 포함
        :param password: string
        :return: 암호화된 비밀번호
        """
        if len(password) < 6:
            raise ValidationError("비밀번호는 6자 이상이어야 합니다.")

        if any(pw.isdigit() for pw in password):
            return password
        else:
            raise ValidationError("비밀번호에는 1개이상의 숫자가 포함되어야 합니다.")

    def validate_title(self, title: str):
        """
        제목 유효성 검사
            - 최대 20자 제하
        :param title: string
        :return: title
        """
        if len(title) > 20:
            raise ValidationError("제목은 최대 20자 까지만 쓸 수 있습니다.")
        return title

    def validate_content(self, content: str):
        """
        본문 유효성 검사
            - 최대 200자 제한
        :param content: string
        :return: content
        """
        if len(content) > 200:
            raise ValidationError("본문은 최대 200자 까지만 쓸 수 있습니다.")
        return content

    def create(self, validated_data):
        """
        일반 비밀번호에서 암호화된 비밀번호로 변경하여 게시물 저장
        :param validated_data:
        :return: Created posting object
        """
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.password = hash_password(password)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        """
        암호화된 비밀번호로 게시글 인스턴스 수정
        :param instance:
        :param validated_data:
        :return: instance
        """
        password = validated_data.pop("password")
        if not check_password(password, instance):
            raise ValidationError("비밀번호가 맞지 않습니다.")

        instance.password = hash_password(password)
        return super().update(instance, validated_data)
