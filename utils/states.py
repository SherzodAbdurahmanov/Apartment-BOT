from telebot.handler_backends import State, StatesGroup

class AddApartmentState(StatesGroup):
    photo = State()
    city = State()
    address = State()
    description = State()
    price = State()
    contact = State()

class RentApartmentState(StatesGroup):
    city = State()
