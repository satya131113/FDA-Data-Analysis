import pandas as pd

def read_data(path: str):
    # Load custom data
    df = pd.read_csv(path)
    df['recall_initiation_year'] = df['recall_initiation_date'].astype(str).str[:4]
    df['report_year'] = df['report_date'].astype(str).str[:4]
    df['termination_year'] = df['termination_date'].astype(str).str[:4]

    # Convert the extracted year columns to integers, handling NA values
    df['recall_initiation_year'] = pd.to_numeric(df['recall_initiation_year'], errors='coerce')
    df['report_year'] = pd.to_numeric(df['report_year'], errors='coerce')
    df['termination_year'] = pd.to_numeric(df['termination_year'], errors='coerce')
    df['termination_duration_years'] = pd.to_numeric(df['days_to_termination'], errors='coerce') / 365

    df['reason_for_recall'] = df['reason_for_recall'].replace({
        "Penicillin Cross Contamination: All lots of all products repackaged and distributed between 01/05/12 and 02/12/15 are being recalled because they were repackaged in a facility with penicillin products without adequate separation which could introduce the potential for cross contamination with penicillin.": "Penicillin Cross Contamination",
        "Lack of Assurance of Sterility; FDA inspection identified GMP violations potentially impacting product quality and sterility": "Lack of Assurance of Sterility",
        "Lack of sterility assurance.": "Lack of Assurance of Sterility",
        "The firm received seven reports of adverse reactions in the form of skin abscesses potentially linked to compounded preservative-free methylprednisolone 80mg/ml 10 ml vials.": "Adverse Reactions",
        "CGMP Deviations: Intermittent exposure to temperature excursion during storage.": "CGMP Deviations (Deviated from regulations)"
    })
    df['initial_firm_notification'] = df['initial_firm_notification'].replace({
        "Two or more of the following: Email, Fax, Letter, Press Release, Telephone, Visit": "Two of listed formats"
    })

    return df