# DashPlotly Project

This project is a data analysis dashboard for visualizing FDA drug recall data from 2006 to 2024. The dashboard is built using Dash and Plotly, providing interactive visualizations and insights into drug recall trends, risk levels, and firm notifications.

The CSV file containing the drug recall data is located at `./datafiles/drug-enforcement-data.csv`. This file is used to load the data into the dashboard for analysis and visualization.

## Data Columns and Explanation

The dataset used in this project contains several columns, each providing specific information about the drug recalls. Below is a list of these columns along with an explanation of each:

- **Status**: The current status of the recall, indicating whether it is ongoing, completed, or terminated.
- **City**: The city where the recalling firm is located.
- **State**: The state where the recalling firm is located.
- **Country**: The country where the recalling firm is located.
- **Classification**: The classification of the recall, which typically indicates the level of health hazard posed by the product being recalled:
  1. **Class I** - A situation in which there is a reasonable probability that the use of, or exposure to, a violative product will cause serious adverse health consequences or death.
  2. **Class II** - A situation in which use of, or exposure to, a violative product may cause temporary or medically reversible adverse health consequences or where the probability of serious adverse health consequences is remote.
  3. **Class III** - A situation in which use of, or exposure to, a violative product is not likely to cause adverse health consequences.
- **Product Type**: The type of product being recalled, such as a drug, device, or food product.
- **Recalling Firm**: The name of the firm that is recalling the product.
- **Initial Firm Notification**: The method which the recalling firm was initially notified about the issue leading to the recall.
- **Distribution Pattern**: The pattern or scope of distribution for the recalled product, indicating where the product was distributed.
- **Product Description**: A description of the product being recalled, including details like brand name, dosage form, etc.
- **Product Quantity**: The quantity of the product that is being recalled.
- **Reason for Recall**: The reason why the product is being recalled, such as contamination, mislabeling, or safety concerns.
- **Recall Initiation Date**: The date when the recall was initiated.
- **Report Date**: The date when the recall was reported to the relevant authorities.
- **Termination Date**: The date when the recall was officially terminated or completed.
- **Days to Termination**: The number of days between the recall initiation date and the termination date, indicating the duration of the recall process.

## Findings

- **Class II Recalls**: The majority of recalled drugs are of Class II, indicating a mid-level risk with reversible effects. A notable change in trend is observed after 2017, with a significant increase in Class I recalls, which pose serious risks.
- **Recall Termination Duration**: On average, it takes about 20 months for a drug recall to be terminated. A concerning observation is the spike in Class I terminations, which at one point surpassed the terminations of Class II drugs.
- **Geographical Trends**: While the majority of recalls are from the United States, excluding the US reveals significant recalls from Canada, China, and India. Further excluding Canada highlights Mexico, Germany, and Jordan as countries with notable drug recalls by the FDA.
- **Notification Methods**: Interestingly, the primary method for notifying firms about recalls is through letters, despite the availability of faster communication methods like email, fax, or telephone.

## Python Version

This project requires Python 3.13.1.

## Steps to Replicate

1. **Clone the Repository**:
   ```bash
   git clone [repository-url](https://github.com/satya131113/FDA-Data-Analysis)
   cd DashPlotly
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Start the Dash application by running:
   ```bash
   python main.py
   ```

5. **Access the Dashboard**:
   Open your web browser and go to `http://127.0.0.1:8050` to view the dashboard.

## Data Source

The data used in this project is sourced from the [FDA's official website](https://open.fda.gov/data/downloads).

## Additional Resources

For more detailed information on data definitions, you can refer to the following resources:
- [Enforcement Report API Definitions](https://www.fda.gov/safety/enforcement-reports/enforcement-report-api-definitions)
- [Enforcement Report Information and Definitions](https://www.fda.gov/safety/enforcement-reports/enforcement-report-information-and-definitions)


## License

The project uses the MIT License, a permissive free software license. For more information, refer to the [LICENSE](LICENSE) file.

