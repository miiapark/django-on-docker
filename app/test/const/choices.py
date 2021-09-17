from django.db import models


class CampaignMessageType(models.IntegerChoices):
    """
    캠페인 메시지 타입
    """
    ADVERTISING = (0, "광고성 메시지")
    NORMAL = (1, "일반 메시지")
    PRIVATE_INFORMATION = (2, "개인정보 이용 알림")
    MARKETING_CONSENT = (3, "마케팅 수신동의 알림")
    FIRST_PAYMENT = (4, "첫 결제 3일전 알림")
    ROUTINE_ALARM = (5, "독서 루틴 알림")
    TEST = (99, "테스트 메시지")
