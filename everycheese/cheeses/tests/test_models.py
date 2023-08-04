from everycheese.cheeses.models import Cheese
import pytest
pytestmark = pytest.mark.django_db


def test___str__():
    cheese = Cheese.objects.create(
        name="Vegan Pepperjack",
        description="Spicy and creamy",
        firmness=Cheese.Firmness.SEMI_SOFT,
        slug="vegan-pepperjack",
    )
    assert cheese.__str__() == "Vegan Pepperjack"
    assert str(cheese) == "Vegan Pepperjack"
