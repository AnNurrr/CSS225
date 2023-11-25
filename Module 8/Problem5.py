# Ainur
# 11/25/2023

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_weaknesses(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

def check_task_completion(character, task_name, required_items, required_debuff=None):
    if all(item in character.get_weapons() for item in required_items) and \
            (required_debuff is None or required_debuff not in character.get_weaknesses()):
        print(f"{character.get_nickname()} has completed the task: {task_name}")
    else:
        print(f"{character.get_nickname()} is not ready for the task: {task_name}")


player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])


tasks = {
    'Climb a mountain': (['rope', 'coat', 'first aid kit'], 'slow'),
    'Cook a meal': (['pan', 'groceries'], 'small'),
    'Write a book': (['pen', 'paper', 'idea'], 'confusion'),
}


for task_name, (required_items, required_debuff) in tasks.items():
    check_task_completion(player1, task_name, required_items, required_debuff)
