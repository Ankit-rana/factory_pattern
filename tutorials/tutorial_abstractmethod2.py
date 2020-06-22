from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def work(self):
        raise NotImplementedError

class NormalProduct(Product):
    def work(self):
        return "completed successfully"


if __name__ == '__main__':
    # print(type(Product()))
    # print(type(Product))
    print(NormalProduct().work())
