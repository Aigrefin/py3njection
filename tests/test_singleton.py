from unittest import TestCase
from unittest.mock import Mock

from multiprocessing import RLock

import py3njection
from py3njection import singleton


@singleton
class Singleton:
    pass


class TestSingleton(TestCase):
    def test_shouldReturnSameInstance_OfTheDecoratedClass(self):
        # Given
        first_instance = Singleton._instance_factory()

        # When
        second_instance = Singleton._instance_factory()

        # Then
        self.assertIsInstance(first_instance, Singleton)
        self.assertEqual(second_instance, first_instance)

    def test_shouldUseRLock(self):
        # Given
        rlock = Mock(RLock())
        py3njection.singleton_decorator.lock = rlock

        # When
        py3njection.singleton_decorator._set_singleton_instance(Mock())

        # Then
        rlock.acquire.assert_called_with()
        rlock.release.assert_called_with()
