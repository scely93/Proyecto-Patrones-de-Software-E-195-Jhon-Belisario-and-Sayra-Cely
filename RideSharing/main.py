#Jhon Belisario - Sayra Cely
from core.ride_sharing_system import RideSharingSystem


def main():
    system_1 = RideSharingSystem()
    system_2 = RideSharingSystem()

    print(system_1.get_name())

    print("¿Es la misma instancia?")
    print(system_1 is system_2)


if __name__ == "__main__":
    main()