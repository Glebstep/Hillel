from .models import MenuItem, Category, OrderModel
from abc import ABC, abstractmethod
#Abstract_method 
class AbstractFactory(ABC):
    @abstractmethod
    def create_menu_item(self, **kwargs):
        pass

    @abstractmethod
    def create_category(self, **kwargs):
        pass

    @abstractmethod
    def create_order(self, **kwargs):
        pass
    

class ConcreteFactory:
    def create_menu_item(self, **kwargs):
        return MenuItem.objects.create(**kwargs)

    def create_category(self, **kwargs):
        return Category.objects.create(**kwargs)

    def create_order(self, **kwargs):
        return OrderModel.objects.create(**kwargs)