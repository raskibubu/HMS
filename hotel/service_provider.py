from dependency_injector import containers, providers

from hotel.repository.CustomerRepository import CustomerRepository, DjangoORMACustomerRepository
from hotel.services.CustomerManagementService import CustomerManagementService, \
    DefaultCustomerManagementService

from hotel.repository.ManagerRepository import ManagerRepository, DjangoORMAManagerRepository
from hotel.services.ManagerManagementService import ManagerManagementService, \
    DefaultManagerManagementService

from hotel.repository.RoomRepository import RoomRepository, DjangoORMARoomRepository
from hotel.services.RoomsManagementService import RoomManagementService, \
    DefaultRoomManagementService

from hotel.repository.BookingRepository import BookingRepository, DjangoORMABookingRepository
from hotel.services.BookingManagementService import BookingManagementService, \
    DefaultBookingManagementService
from typing import Callable

from hotel.repository.PaymentRepository import PaymentRepository, DjangoORMAPaymentRepository
from hotel.services.PaymentManagementService import PaymentManagementService, \
    DefaultPaymentManagementService

from hotel.repository.GuestRepository import GuestRepository, DjangoORMAGuestRepository
from hotel.services.GuestManagementService import GuestManagementService, \
    DefaultGuestManagementService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    customer_repository: Callable[[], CustomerRepository] = providers.Factory(
        DjangoORMACustomerRepository
    )

    customer_management_service: Callable[[], CustomerManagementService] = providers.Factory(
        DefaultCustomerManagementService,
        repository=customer_repository
    )

    manager_repository: Callable[[], ManagerRepository] = providers.Factory(
        DjangoORMAManagerRepository
    )

    manager_management_service: Callable[[], ManagerManagementService] = providers.Factory(
        DefaultManagerManagementService,
        repository=manager_repository

    )

    room_repository: Callable[[], RoomRepository] = providers.Factory(
        DjangoORMARoomRepository
    )

    room_management_service: Callable[[], RoomManagementService] = providers.Factory(
        DefaultRoomManagementService,
        repository=room_repository
    )

    booking_repository: Callable[[], BookingRepository] = providers.Factory(
        DjangoORMABookingRepository
    )

    booking_management_service: Callable[[], BookingManagementService] = providers.Factory(
        DefaultBookingManagementService,
        repository=booking_repository
    )

    payment_repository: Callable[[], PaymentRepository] = providers.Factory(
        DjangoORMAPaymentRepository
    )

    payment_management_service: Callable[[], PaymentManagementService] = providers.Factory(
        DefaultPaymentManagementService,
        repository=payment_repository
    )

    guest_repository: Callable[[], GuestRepository] = providers.Factory(
        DjangoORMAGuestRepository
    )

    guest_management_service: Callable[[], GuestManagementService] = providers.Factory(
        DefaultGuestManagementService,
        repository=guest_repository
    )


hms_service_provider = Container()
