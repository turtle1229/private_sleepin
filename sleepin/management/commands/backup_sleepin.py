import csv
import datetime
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Sleeptime, Meal, Health, Diary


class Command(BaseCommand):
    help = "Backup sleeptime data"

    def handle(self, *args, **options):
        # 実行時のYYYYMMDDを取得
        date = datetime.date.today().strftime("%Y%m%d")

        # 保存ファイルの相対パス
        file_path_slt = settings.BACKUP_PATH + "slt_" + date + ".csv"
        file_path_meal = settings.BACKUP_PATH + "meal_" + date + ".csv"
        file_path_hlt = settings.BACKUP_PATH + "hlt_" + date + ".csv"
        file_path_diary = settings.BACKUP_PATH + "diary_" + date + ".csv"

        # 保存ディレクトリが存在しなければ作成
        os.makedirs(settings.BACKUP_PATH, exist_ok=True)

        # Sleeptimeバックアップファイルの作成
        with open(file_path_slt, "w", newline="") as file:
            writer = csv.writer(file)

            # ヘッダーの書き込み
            header = [field.name for field in Sleeptime._meta.fields]
            writer.writerow(header)

            # Sleeptimeテーブルの全データを取得
            sleeptimes = Sleeptime.objects.all()

            # データ部分の書き込み
            for sleeptime in sleeptimes:
                writer.writerow([str(sleeptime.user),
                                 str(sleeptime.create_date),
                                 str(sleeptime.sleep_at),
                                 str(sleeptime.wakeup_at)])

        # 保存ディレクトリディレクトリのファイルリストを取得
        files = os.listdir(settings.BACKUP_PATH)
        # ファイルが設定数以上あったら一番古いファイルを削除
        if len(files) >= settings.NUM_SAVED_BACKUP:
            files.sort()
            os.remove(settings.BACKUP_PATH + files[0])


        # Mealバックアップファイルの作成
        with open(file_path_meal, "w", newline="") as file:
            writer = csv.writer(file)

            # ヘッダーの書き込み
            header = [field.name for field in Meal._meta.fields]
            writer.writerow(header)

            # mealテーブルの全データを取得
            meals = Meal.objects.all()

            # データ部分の書き込み
            for meal in meals:
                writer.writerow([str(meal.user),
                                 str(meal.create_date),
                                 meal.meal,
                                 meal.meal_menu])

        # 保存ディレクトリディレクトリのファイルリストを取得
        files = os.listdir(settings.BACKUP_PATH)
        # ファイルが設定数以上あったら一番古いファイルを削除
        if len(files) >= settings.NUM_SAVED_BACKUP:
            files.sort()
            os.remove(settings.BACKUP_PATH + files[0])

        # Healthバックアップファイルの作成
        with open(file_path_hlt, "w", newline="") as file:
            writer = csv.writer(file)

            # ヘッダーの書き込み
            header = [field.name for field in Health._meta.fields]
            writer.writerow(header)

            # healthテーブルの全データを取得
            healths = Health.objects.all()

            # データ部分の書き込み
            for health in healths:
                writer.writerow([str(health.user),
                                 str(health.create_date),
                                 health.health,
                                 health.health_menu])

        # 保存ディレクトリディレクトリのファイルリストを取得
        files = os.listdir(settings.BACKUP_PATH)
        # ファイルが設定数以上あったら一番古いファイルを削除
        if len(files) >= settings.NUM_SAVED_BACKUP:
            files.sort()
            os.remove(settings.BACKUP_PATH + files[0])

        # Diaryバックアップファイルの作成
        with open(file_path_diary, "w", newline="") as file:
            writer = csv.writer(file)

            # ヘッダーの書き込み
            header = [field.name for field in Diary._meta.fields]
            writer.writerow(header)

            # diaryテーブルの全データを取得
            diaries = Diary.objects.all()

            # データ部分の書き込み
            for diary in diaries:
                writer.writerow([str(diary.user),
                                 diary.title,
                                 diary.content,
                                 diary.photo1,
                                 diary.photo2,
                                 diary.photo3,
                                 str(diary.created_at),
                                 str(diary.updated_at)])

        # 保存ディレクトリディレクトリのファイルリストを取得
        files = os.listdir(settings.BACKUP_PATH)
        # ファイルが設定数以上あったら一番古いファイルを削除
        if len(files) >= settings.NUM_SAVED_BACKUP:
            files.sort()
            os.remove(settings.BACKUP_PATH + files[0])
