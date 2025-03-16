from datetime import datetime, date
import time

from mutationtracker import MutationTrackedObject


class Person(MutationTrackedObject):

    _mutations_log_function = print  # optional attribute, remove for no console output

    def __init__(
        self,
        social_security_number,
        name,
        gender,
        date_of_birth,
        children,
        date_of_death=None,
    ):
        self.social_security_number = social_security_number
        self.name = name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death
        self.children = children

    def have_child(
        self, social_security_number, name, gender, date_of_birth=datetime.now().date()
    ):
        baby = Person(social_security_number, name, gender, date_of_birth, [])
        self.children = self.children + [baby]

    def adopt_child(
        self, social_security_number, name, gender, date_of_birth=datetime.now().date()
    ):
        child = Person(social_security_number, name, gender, date_of_birth, [])
        self.children = self.children + [child]

    def __repr__(self):
        return f"{self.social_security_number} - {self.name}"


def main():
    #  ========== Example: init of Alice ==========
    print("========== Example: init of Alice ==========")
    example_person = Person(12345678901, "Alice", "Female", date(1990, 3, 7), [])

    #  ========== Example: children ==========
    print("\n========== Example: children ==========")
    #  might one day have children herself
    example_person.have_child(12312312301, "Charles", "Male")
    example_person.have_child(12312312302, "Davey", "Male")
    #  might also adopt one more
    example_person.adopt_child(
        99889988771, "Fatima", "Female", date_of_birth=date(2024, 2, 2)
    )
    #  might find out Charles is actually a different baby because of a hospital mix-up
    #  so put him up for adoption as he is not as enjoyable

    def get_rid_of_child(person, name):
        person.children = [c for c in person.children if c.name != name]

    get_rid_of_child(example_person, "Charles")

    #  ========== Example: gender ==========
    print("\n========== Example: gender ==========")
    #  is her gender right? might change

    def change_gender(person, new_name, new_gender):
        """Might one day find out something is off but that can be changed"""
        time.sleep(0.1)  # takes some time
        person.name = new_name
        person.gender = new_gender

    #  actually, she feels like he and continues as Bob
    change_gender(example_person, "Bob", "Male")
    #  Might regret that later, and actually convert back
    change_gender(example_person, "Alice", "Female")

    #  ========== Example: safari trip gone wrong ==========
    print("\n========== Example: safari trip gone wrong ==========")
    #  live is an adventure, so go on a nice safari trip

    def go_on_safari(person):
        """Go on a nice and safe safari trip, so better be careful, right?"""
        pet_lion(person)

    def pet_lion(person):
        """Do not try this at home, or at the zoo, or while on safari, or anywhere ever, it might end badly"""
        person.date_of_death = datetime.now().date()

    go_on_safari(example_person)

    #  ========== Example: log full history of Alice ==========
    print("\n========== Example: log full history of Alice ==========")
    example_person.log_all_mutations()

    return example_person


if __name__ == "__main__":
    main()
