class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"

        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0

        for worker in self.workers:
            salaries += worker.salary

        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_needs = 0

        for animal in self.animals:
            animal_needs += animal.money_for_care

        if animal_needs <= self.__budget:
            self.__budget -= animal_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []

        result = f"You have {len(self.animals)} animals\n"

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        result += f"----- {len(lions)} Lions:\n"

        for lion in lions:
            result += f"{repr(lion)}\n"

        result += f"----- {len(tigers)} Tigers:\n"

        for tiger in tigers:
            result += repr(tiger) + "\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"

        for cheetah in cheetahs:
            result += f"{repr(cheetah)}\n"

        return result.strip()

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []

        result = f"You have {len(self.workers)} workers\n"

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)

        result += f"----- {len(keepers)} Keepers:\n"

        for keeper in keepers:
            result += f"{repr(keeper)}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"

        for caretaker in caretakers:
            result += f"{repr(caretaker)}\n"

        result += f"----- {len(vets)} Vets:\n"

        for vet in vets:
            result += f"{repr(vet)}\n"

        return result.strip()
