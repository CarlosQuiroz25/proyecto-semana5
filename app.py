class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f'El vehiculo {self.brand} ha sido vendido')
        else:
            print(f'El vehiculo {self.brand} no está disponible')

    def check_availability(self):
        if self.is_available:
            print(f'El vehiculo {self.brand} está disponible')
        else:
            print(f'El vehiculo {self.brand} no está disponible')

    def get_price(self):
        return f'El precio del vehiculo es: ${self.price}'

    def start_engine(self):
        raise NotImplementedError('Este método debe ser implementado en las subclases')

    def stop_engine(self):
        raise NotImplementedError('Este método debe ser implementado en las subclases')

class Car(Vehicle):
    def __init__(self, brand, model, price, num_doors):
        super().__init__(brand, model, price)
        self.num_doors = num_doors

    def start_engine(self):
        if not self.is_available:
            print(f'El carro {self.brand} ha arrancado')
        else:
            print(f'El carro {self.brand} no está disponible')

    def stop_engine(self):
        if not self.is_available:
            print(f'El carro {self.brand} ha parado')
        else:
            print(f'El carro {self.brand} no está disponible')

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            print(f'La bicicleta {self.brand} ha arrancado')
        else:
            print(f'La bicicleta {self.brand} no está disponible')

    def stop_engine(self):
        if not self.is_available:
            print(f'La bicicleta {self.brand} ha parado')
        else:
            print(f'La bicicleta {self.brand} no está disponible')

class Truck(Vehicle):
    def __init__(self, brand, model, price, load_capacity):
        super().__init__(brand, model, price)
        self.load_capacity = load_capacity

    def start_engine(self):
        if not self.is_available:
            print(f'El camión {self.brand} ha arrancado')
        else:
            print(f'El camión {self.brand} no está disponible')

    def stop_engine(self):
        if not self.is_available:
            print(f'El camión {self.brand} ha parado')
        else:
            print(f'El camión {self.brand} no está disponible')

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.purcharsed_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.is_available:
            vehicle.sell()
            self.purcharsed_vehicles.append(vehicle)
        else:
            print(f'El vehiculo {vehicle.brand} no está disponible')

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.chech_availability():
            print(f'El vehiculo {vehicle.brand} está disponible')
        else:
            print(f'El vehiculo {vehicle.brand} no está disponible')

    def get_purcharsed_vehicles(self):
        return self.purcharsed_vehicles

class Dealership:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        print(f'El vehiculo {vehicle.brand} ha sido agregado a la tienda')

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            print(f'El vehiculo {vehicle.brand} ha sido eliminado de la tienda')
        else:
            print(f'El vehiculo {vehicle.brand} no está en la tienda')

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f'El cliente {customer.name} ha sido registrado en la tienda')

    def remove_customer(self, customer: Customer):
        if customer in self.customers:
            self.customers.remove(customer)
            print(f'El cliente {customer.name} ha sido eliminado de la tienda')

        else:
            print(f'El cliente {customer.name} no está en la tienda')

    def show_vehicles(self):
        print('Los vehiculos disponibles son:')
        for vehicle in self.vehicles:
            if vehicle.check_availability():
                print(f'- {vehicle.brand} -- ${vehicle.price}')

car1 = Car('Toyota', 'Corolla', 20000, 4)
bike1 = Bike('Honda', 'CBR', 10000)
truck1 = Truck('Ford', 'F-150', 50000, 2000)

customer1 = Customer('Juan', 25)

dealership = Dealership()
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)
dealership.register_customer(customer1)

customer1.buy_vehicle(car1)
