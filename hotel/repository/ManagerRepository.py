from abc import abstractmethod, ABCMeta
from typing import List

from django.contrib.auth.models import User, Group

from hotel.models import Manager
from hotel.dto.ManagerDto import *


class ManagerRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_manager(self, model: RegisterManager) -> int:
        """creates a customer model"""
        raise NotImplementedError

    @abstractmethod
    def list_managers(self) -> List[ListManagers]:
        """list customer models"""
        raise NotImplementedError

    @abstractmethod
    def get_details_by_manager(self, user_id: int) -> ManagerDetails:
        raise NotImplementedError


class DjangoORMAManagerRepository(ManagerRepository):
    def create_manager(self, model: RegisterManager) -> int:
        manager = Manager()
        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

        manager.user = user
        group = Group.objects.get(name="Managers")
        user.groups.add(group)

        manager.address = model.address
        manager.phone_number = model.phone_number
        manager.date_of_birth = model.date_of_birth
        manager.save()
        manager_id = manager.id
        return manager_id

    def list_managers(self) -> List[ListManagers]:
        managers = list(
            Manager.objects.values('id', 'user__username', 'user__first_name', 'user__last_name',
                                   'phone_number'))
        results: List[ListManagers] = []

        for manager in managers:
            item = ListManagers()
            item.id = manager['id']
            item.phone_number = manager['phone_number']
            item.first_name = manager['user__first_name']
            item.last_name = manager['user__last_name']
            item.username = manager['user__username']
            results.append(item)
        return results

    def get_details_by_manager(self, user_id: int) -> ManagerDetails:
        manager = Manager.objects.values("user_id", "user__first_name", "user__last_name",
                                         "user__username", "user__email", "address", "phone_number",
                                         "date_of_birth").get(
            user_id=user_id)
        item = ManagerDetails()
        try:
            item.id = manager['user_id']
            item.first_name = manager['user__first_name']
            item.last_name = manager['user__last_name']
            item.username = manager['user__username']
            item.email = manager['user__email']
            item.address = manager['address']
            item.phone_number = manager['phone_number']
            item.date_of_birth = manager['date_of_birth']
            return item
        except Manager.DoesNotExist as e:
            raise e
