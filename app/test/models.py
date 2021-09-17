from django.db import models
from core import models as core_models
from test.const.choices import CampaignMessageType


class Message(core_models.TimeStampedModel):
    msg_id = models.AutoField(db_column="msg_id", primary_key=True, help_text="캠페인 메시지 시퀀스")
    msg_type = models.PositiveSmallIntegerField(db_column="msg_type",
                                                choices=CampaignMessageType.choices,
                                                default=CampaignMessageType.NORMAL,
                                                help_text="캠페인 메시지 타입")

    class Meta:
        managed = True
        db_table = "campaign_message"
