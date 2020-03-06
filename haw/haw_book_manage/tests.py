from faker import Factory
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Book

fake = Factory.create('ja_JP')


class CreateTestData:
    # テストデータの作成
    def data_create(self):
        Book.objects.create(
            title=fake.country(),
            author=fake.name(),
            publisher=fake.company(),
            finished_date=fake.date(pattern='%Y-%m-%d', end_datetime=None),
            created_at=timezone.now(),
            updated_at=timezone.now()
        )


class BookTopTest(TestCase):
    # top画面のアクセステスト
    def test_top(self):
        res = self.client.get(reverse('haw:top'))
        self.assertEqual(res.status_code, 200)
        self.assertQuerysetEqual(res.context['books'], [])


class BookCreateTest(TestCase):
    # データ登録テスト
    def test_create(self):
        create_data = {
            'title': fake.country(),
            'author': fake.name(),
            'publisher': fake.company(),
            'finished_date': fake.date(pattern='%Y-%m-%d', end_datetime=None),
            'created_at': timezone.now(),
            'updated_at': timezone.now()
        }
        res = self.client.post(
            reverse('haw:create'),
            data=create_data
        )
        self.assertEqual(res.status_code, 302)


class BookUpdateTest(TestCase):
    # データ更新テスト(成功)
    def test_update(self):
        create_test_data = CreateTestData()
        create_test_data.data_create()

        update_data = {
            'title': fake.country(),
            'author': fake.name(),
            'publisher': fake.company(),
            'finished_date': fake.date(pattern='%Y-%m-%d', end_datetime=None),
        }
        res = self.client.post(
            reverse('haw:update', kwargs={'book_id': 1}),
            data=update_data
        )
        self.assertEqual(res.status_code, 302)

    # データ更新テスト(対象データが無い)
    def test_update_fail_target_data_not_exist(self):
        create_test_data = CreateTestData()
        create_test_data.data_create()

        update_data = {
            'title': fake.country(),
            'author': fake.name(),
            'publisher': fake.company(),
            'finished_date': fake.date(pattern='%Y-%m-%d', end_datetime=None),
        }
        with self.assertRaises(Exception):
            self.client.post(
                reverse('haw:update', kwargs={'book_id': 999}),
                data=update_data
            )

    # データ更新テスト(失敗：タイトルがnull)
    def test_update_fail_title_null(self):
        create_test_data = CreateTestData()
        create_test_data.data_create()

        update_data = {
            'title': None,
        }
        with self.assertRaises(Exception):
            self.client.post(
                reverse('haw:update', kwargs={'book_id': 1}),
                data=update_data
            )

    # データ更新テスト(失敗：著者がnull)
    def test_update_fail_author_null(self):
        create_test_data = CreateTestData()
        create_test_data.data_create()

        update_data = {
            'author': None,
        }
        with self.assertRaises(Exception):
            self.client.post(
                reverse('haw:update', kwargs={'book_id': 1}),
                data=update_data
            )

    # データ更新テスト(失敗：出版社がnull)
    def test_update_fail_publisher_null(self):
        create_test_data = CreateTestData()
        create_test_data.data_create()

        update_data = {
            'title': None,
        }
        with self.assertRaises(Exception):
            self.client.post(
                reverse('haw:update', kwargs={'book_id': 1}),
                data=update_data
            )

    # データ更新テスト(失敗：読了日がnull)
    def test_update_fail_finished_date_null(self):
        create_test_data = CreateTestData()
        create_test_data.data_create()

        update_data = {
            'finished_date': None,
        }
        with self.assertRaises(Exception):
            self.client.post(
                reverse('haw:update', kwargs={'book_id': 1}),
                data=update_data
            )


class BookDeleteTest(TestCase):

    # データ削除テスト(成功)
    def test_delete(self):
        create_test_data = CreateTestData()
        create_test_data.data_create()

        res = self.client.post(
            reverse('haw:delete', kwargs={'book_id': 1})
        )
        self.assertEqual(res.status_code, 302)

    # データ削除テスト(失敗：対象データ無し)
    def test_delete_fail_target_data_not_exist(self):
        create_test_data = CreateTestData()
        create_test_data.data_create()

        with self.assertRaises(Exception):
            self.client.post(
                reverse('haw:delete', kwargs={'book_id': 999})
            )
