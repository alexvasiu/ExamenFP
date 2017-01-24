"""
    Aici se lanseaza programul :
        - se ruleaza testele
        - se creeaza controlere
        - se creeaza repository
        - se creeaza validator
        - se apeleaza functia de show din UI pentru a pornii aplicatia
"""

from Controller.EventsController import EventsController
from Controller.PersonsController import PersonsController
from Domain.Validator import Validator
from Repository.Repo import Repo
from Repository.DatabaseRepo import RepoDB
from Repository.RepoMemory import RepoMemory
from Tests.Tests import Tests
from UI.UI import UI


if __name__ == "__main__":
    #tests = Tests()
    #tests.run_all()
    cmd = input("Choose your repository type :\n1 - Memory Repository\n2 - File Repository\n3 - Database Repository\n")
    repo = None
    if cmd == '1':
        repo = RepoMemory()
    elif cmd == '2':
        repo = Repo(["Repository/persons.txt", "Repository/events.txt", "Repository/register.txt"])
    elif cmd == '3':
        repo = RepoDB("Repository/data.sqlite")
    if repo is not None:
        validator = Validator()
        Persons = PersonsController(repo, validator)
        Events = EventsController(repo, validator)
        interfata = UI(Persons, Events)
        interfata.show()

# tema 7 - backtracking