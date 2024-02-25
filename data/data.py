from dataclasses import dataclass, field
from string import ascii_lowercase

from faker import Faker


faker = Faker()


@dataclass
class Customer:
    post_code: int = field(default_factory=lambda: faker.random_number(digits=10))
    last_name: str = field(default_factory=lambda: faker.last_name())

    def __post_init__(self):
        post_code_str = str(self.post_code)
        self.first_name = ""

        for index in range(0, len(post_code_str), 2):  # формирование имени на основании почтового кода
            letter_index = int(post_code_str[index: index+2]) % 26
            self.first_name += ascii_lowercase[letter_index]
        self.first_name = self.first_name.capitalize()
