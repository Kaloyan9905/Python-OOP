from gym.customer import Customer
from gym.equipment import Equipment
from gym.exercise_plan import ExercisePlan
from gym.subscription import Subscription
from gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ""

        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                result += repr(subscription) + "\n"

        for customer in self.customers:
            if customer.id == subscription_id:
                result += repr(customer) + "\n"

        for trainer in self.trainers:
            if trainer.id == subscription_id:
                result += repr(trainer) + "\n"

        for equipment in self.equipment:
            if equipment.id == subscription_id:
                result += repr(equipment) + "\n"

        for plan in self.plans:
            if plan.id == subscription_id:
                result += repr(plan) + "\n"

        return result


