"""
    App Controller
"""

from Controller.ControllerJucatori import ControllerJucator
from Repository.Repo import Repo
from Domain.Validator import Validator
from UI.ui import UI

if __name__ == "__main__":
    repo = Repo("Repository/players.txt")
    validator = Validator()
    controller = ControllerJucator(validator, repo)
    ui = UI(controller)
    ui.showUI()