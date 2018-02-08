import unittest
from app.models import User


class UserTest(unittest.TestCase):
    def test_should_add_user(self):
        username = 'user1'
        password = 'password1'
        user = User()

        self.assertEqual(user.add(username, password), True)

        user.delete(username)


    def test_should_not_add_already_registered_user(self):
        username = 'user1'
        password = 'password1'
        user = User()

        self.assertEqual(user.add(username, password), True)
        self.assertEqual(user.add(username, password), False)

        user.delete(username)


if __name__ == '__main__':
    unittest.main()