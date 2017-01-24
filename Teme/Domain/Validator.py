"""
    Domamin Layer: Validator
"""
class Validator:
    """
        Validator Class
    """
    def validateTema(self, tema):
        """
            validare tema ... se arunca exceptii daca:
                - id nu e numar pozitiv
                - nume student nu are cel putin 3 caractere
                - rezolvarea nu are cel putin 5 cuvinte
        """
        errors = []
        try:
            value_id = int(tema.getID)
            if value_id < 0:
                errors.append("ID is not a positive integer")
        except:
            errors.append("ID is not a valid integer")
        if len(tema.getNumeStudent) < 3:
            errors.append("Name should have minimum 3 letters")
        if len(tema.getRezolvare.split(' ')) < 5:
            errors.append("Solution should have minimum 5 words")
        if len(errors) > 0:
            raise ValueError(str(errors))