from unittest import TestCase
from unittest.mock import Mock

from py3njection import inject


class ToInject:
    def return_type(self):
        return ToInject


class ToInjectWithInstanceFactory:
    @classmethod
    def _instance_factory(cls):
        return 'special instance'


class BeingInjected:
    @inject
    def __init__(self, to_inject: ToInject):
        self.to_inject = to_inject

    def call_dependency(self):
        return self.to_inject.return_type()

    @inject
    def use_dependency(self, to_inject: ToInject):
        return to_inject.return_type()

    @inject
    def use_scoped_dependency(self, to_inject: ToInjectWithInstanceFactory):
        return to_inject


class TestInject(TestCase):
    def test_injectObject_inConstructor_whenNotOverrided(self):
        # When
        being_injected = BeingInjected()

        # Then
        result = being_injected.call_dependency()
        self.assertEqual(result, ToInject)

    def test_doNotInjectObject_inConstructor_WhenOverrided(self):
        # Given
        mock = Mock(ToInject)
        mock.return_type.return_value = str

        # When
        being_injected = BeingInjected(to_inject=mock)

        # Then
        result = being_injected.call_dependency()
        self.assertEqual(result, str)

    def test_injectObject_inMethod_whenNotOverrided(self):
        # Given
        injected = BeingInjected()

        # When
        result = injected.use_dependency()

        # Then
        self.assertEqual(result, ToInject)

    def test_doNotInjectObject_inMethod_whenOverrided(self):
        # Given
        injected = BeingInjected()
        mock = Mock(ToInject)
        mock.return_type.return_value = str

        # When
        result = injected.use_dependency(to_inject=mock)

        # Then
        self.assertEqual(result, str)

    def test_shouldUseInstanceFactory_whenExists(self):
        # Given
        injected = BeingInjected()

        # When
        result = injected.use_scoped_dependency()

        # Then
        self.assertEqual(result, 'special instance')
