from abc import abstractmethod, ABCMeta
from hotel.dto.RoomsDto import *
from hotel.repository.RoomRepository import RoomRepository
from typing import List


class RoomManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_room(self, model: CreateRoom):
        raise NotImplementedError

    @abstractmethod
    def list_rooms(self) -> List[ListRooms]:
        raise NotImplementedError

    @abstractmethod
    def change_room_status(self, model: ChangeRoomStatus):
        raise NotImplementedError

    @abstractmethod
    def change_room_type(self, model: ChangeRoomType):
        raise NotImplementedError

    @abstractmethod
    def get_room_by_room_number(self, room_number: int) -> RoomDetails:
        raise NotImplementedError

    @abstractmethod
    def get_room_by_room_id(self, room_id: int) -> RoomDetails:
        raise NotImplementedError


class DefaultRoomManagementService(RoomManagementService):
    repository = RoomRepository

    def __init__(self, repository: RoomRepository):
        self.repository = repository

    def create_room(self, model: CreateRoom):
        return self.repository.create_room(model)

    def list_rooms(self) -> List[ListRooms]:
        return self.repository.list_rooms()

    def change_room_status(self, model: ChangeRoomStatus):
        return self.repository.change_room_status(model)

    def change_room_type(self, model: ChangeRoomType):
        return self.repository.change_room_type(model)

    def get_room_by_room_number(self, room_number: int) -> RoomDetails:
        return self.repository.get_room_by_room_number(room_number)

    def get_room_by_room_id(self, room_id: int) -> RoomDetails:
        return self.repository.get_room_by_room_id(room_id)

