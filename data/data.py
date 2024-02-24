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
        self.first_name = ''

        while len(post_code_str) > 0:  # формирование имени на основании почтового кода
            index = int(post_code_str[0:2])
            letter = ascii_lowercase[index % 26]
            self.first_name += letter
            post_code_str = post_code_str[2:]
        self.first_name = self.first_name.capitalize()
