from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Sleeptime, Meal, Health, Diary


class LoggedInTestCase(TestCase):
    """各テストクラスで共通の事前準備処理をオーバーライドした独自TestCaseクラス"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""

        #テストユーザーのパスワード
        self.password = 'test0000'

        #各インスタンスメソッドで使うテスト用ユーザーを生成しインスタンス変数に格納しておく
        self.test_user = get_user_model().objects.create_user(
            username='test',
            email='test@2test2.com',
            password=self.password)

        #テスト用ユーザーでログインする
        self.client.login(email=self.test_user.email, password=self.password)


class TestSleeptimeRegisterView(LoggedInTestCase):
    """SleeptimeRegisterView用のテストクラス"""

    def test_register_sleeptime_success(self):
        """睡眠時間登録処理が成功することを検証する"""

        #Postパラメータ
        params = {'create_date': '日付',
                  'sleep_at': '就寝時間',
                  'wakeup_at': '起床時間'}

        #新規睡眠時間登録処理(Post)を実行
        response = self.client.post(reverse_lazy('sleepin:sleeptime_register'), params)

        #登録完了画面へのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('sleepin:registered'))

        #睡眠時間データがDBに登録されたか検証
        self.assertEqual(Sleeptime.objects.filter(create_date='日付').count(), 1)

        def test_register_sleeptime_failure(self):
            """新規睡眠時間登録処理が失敗することを検証する"""

            #新規睡眠時間登録処理(Post)を実行
            response = self.client.post(reverse_lazy('sleepin:sleeptime_register'))

            #必須フォームフィールドが未入力によりエラーになることを検証
            self.assertFormError(response, 'form', 'create_date', 'このフィールドは必須です。')


class TestSleeptimeEditView(LoggedInTestCase):
    """SleeptimeEditView用のテストクラス"""

    def test_edit_sleeptime_success(self):
        """睡眠時間編集処理が成功することを検証する"""

        #テスト用睡眠時間データの作成
        sleeptime = Sleeptime.objects.create(user=self.test_user, create_date='日付編集前')

        #Postパラメータ
        params = {'create_date': '日付編集後'}

        #睡眠時間編集処理（Post）を実行
        response = self.client.post(reverse_lazy('sleepin:sleeptime_edit', kwargs={'pk': sleeptime.pk}), params)

        #睡眠時間詳細画面へのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('sleepin:sleeptime_detail', kwargs={'pk': sleeptime.pk}))

        #睡眠時間データが編集されたかを検証
        self.assertEqual(Sleeptime.objects.get(pk=sleeptime.pk).create_date, '日付編集後')

        def test_edit_sleeptime_failure(self):
            """睡眠時間編集処理が失敗することを検証する"""

            #睡眠時間編集処理（Post）を実行
            response = self.client.post(reverse_lazy('sleepin:sleeptime_edit', kwargs={'pk': 999}))

            #存在しない睡眠時間データを編集しようとしてエラーになることを検証
            self.assertEqual(response.status_code, 404)


