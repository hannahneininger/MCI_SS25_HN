def estimate_max_hr(age_years : int , sex : str) -> int:
    """
    See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
    to estimate the maximum heart rate"""
    if sex == "male":
        max_hr_bpm = 223 - 0.9 * age_years
    elif sex == "female":
        max_hr_bpm = 226 - 1.0 * age_years
    else:
        # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
        max_hr_bpm = input("Enter maximum heart rate:")
    return int(max_hr_bpm)
def build_person(first_name, last_name, sex, age) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    dict = { "first_name" : first_name,
            "last_name" : last_name,
            "age" : age,
            "estimate_max_hr" : estimate_max_hr(age,sex)}
    return dict
def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    dict = {"experiment_name" : experiment_name,
            "date" : date,
            "supervisor" : supervisor,
            "subject" : subject
            }
    return dict

