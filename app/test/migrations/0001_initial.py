# Generated by Django 3.2.6 on 2021-09-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('msg_id', models.AutoField(db_column='msg_id', help_text='캠페인 메시지 시퀀스', primary_key=True, serialize=False)),
                ('msg_type', models.PositiveSmallIntegerField(choices=[(0, '광고성 메시지'), (1, '일반 메시지'), (2, '개인정보 이용 알림'), (3, '마케팅 수신동의 알림'), (4, '첫 결제 3일전 알림'), (5, '독서 루틴 알림'), (99, '테스트 메시지')], db_column='msg_type', default=1, help_text='캠페인 메시지 타입')),
            ],
            options={
                'db_table': 'campaign_message',
                'managed': True,
            },
        ),
    ]
