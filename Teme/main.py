"""
    Aplication Coordinator
"""

from Controller.TemeController import TemeController
from Domain.Validator import Validator
from Repository.Repo import Repo
from UI.UI import UI


if __name__ == "__main__":
    validator = Validator()
    repo = Repo("Repository/teme.txt")
    controller = TemeController(repo, validator)
    menu = UI(controller)
    menu.showMenu()