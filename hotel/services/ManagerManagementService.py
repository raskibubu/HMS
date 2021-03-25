from abc import abstractmethod, ABCMeta
from typing import List
from hotel.repository.ManagerRepository import ManagerRepository
from hotel.dto.ManagerDto import *


class ManagerManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_manager(self, model: RegisterManager) -> int:
        raise NotImplementedError

    @abstractmethod
    def list_managers(self) -> List[ListManagers]:
        raise NotImplementedError

    @abstractmethod
    def get_details_by_manager(self, user_id: int) -> ManagerDetails:
        raise NotImplementedError


class DefaultManagerManagementService(ManagerManagementService):
    repository: ManagerRepository

    def __init__(self, repository: ManagerRepository):
        self.repository = repository

    def create_manager(self, model: RegisterManager) -> int:
        return self.repository.create_manager(model)

    def list_managers(self) -> List[ListManagers]:
        return self.repository.list_managers()

    def get_details_by_manager(self, user_id: int) -> ManagerDetails:
        return self.repository.get_details_by_manager(user_id)

