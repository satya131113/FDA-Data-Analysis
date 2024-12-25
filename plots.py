from dash import html, dcc, callback, Output, Input
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import pandas as pd
from io import BytesIO
import matplotlib
matplotlib.use('Agg')


def create_countries_plot(df):
    # Convert 'report_date' to datetime to extract the year
    df['report_date'] = pd.to_datetime(df['report_date'], format='%Y%m%d')

    # Extract the year from 'report_date'
    df['report_year'] = df['report_date'].dt.year

    # Group by 'country' to get the total count of recalls and select top 5 countries
    top_countries = df['country'].value_counts().nlargest(8).index

    # Filter the dataframe to include only the top 5 countries
    df_top_countries = df[df['country'].isin(top_countries)]

    # Group by 'report_year' and 'country' to get the count of recalls for top 5 countries
    recalls_by_year_country = df_top_countries.groupby(['report_year', 'country']).size().unstack(fill_value=0)

    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))
    recalls_by_year_country.plot(kind='barh', stacked=True, ax=ax, colormap='Set2')
    ax.set_title('Horizontal Bar Chart of Recalls by Year and Top 8 Countries', color='darkblue')
    ax.set_xlabel('Number of Recalls', color='darkgreen')
    ax.set_ylabel('Country', color='darkred')
    ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left', title_fontsize='13', fontsize='11', facecolor='lightyellow')
    plt.tight_layout()

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

def create_countries_plot_excluding_us(df):
    # Convert 'report_date' to datetime to extract the year
    df['report_date'] = pd.to_datetime(df['report_date'], format='%Y%m%d')

    # Extract the year from 'report_date'
    df['report_year'] = df['report_date'].dt.year

    # Exclude the United States from the dataframe
    df = df[df['country'] != 'United States']

    # Group by 'country' to get the total count of recalls and select top 8 countries
    top_countries = df['country'].value_counts().nlargest(8).index

    # Filter the dataframe to include only the top 8 countries
    df_top_countries = df[df['country'].isin(top_countries)]

    # Group by 'report_year' and 'country' to get the count of recalls for top 8 countries
    recalls_by_year_country = df_top_countries.groupby(['report_year', 'country']).size().unstack(fill_value=0)

    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))
    recalls_by_year_country.plot(kind='barh', stacked=True, ax=ax, colormap='Set2')
    ax.set_title('Horizontal Bar Chart of Recalls by Year and Top 8 Countries Excluding US', color='darkblue')
    ax.set_xlabel('Number of Recalls', color='darkgreen')
    ax.set_ylabel('Country', color='darkred')
    ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left', title_fontsize='13', fontsize='11', facecolor='lightyellow')
    plt.tight_layout()

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

def create_countries_plot_excluding_canada(df):
    # Convert 'report_date' to datetime to extract the year
    df['report_date'] = pd.to_datetime(df['report_date'], format='%Y%m%d')

    # Extract the year from 'report_date'
    df['report_year'] = df['report_date'].dt.year

    # Exclude the United States from the dataframe
    df = df[df['country'] != 'Canada']

    # Group by 'country' to get the total count of recalls and select top 8 countries
    top_countries = df['country'].value_counts().nlargest(8).index

    # Filter the dataframe to include only the top 8 countries
    df_top_countries = df[df['country'].isin(top_countries)]

    # Group by 'report_year' and 'country' to get the count of recalls for top 8 countries
    recalls_by_year_country = df_top_countries.groupby(['report_year', 'country']).size().unstack(fill_value=0)

    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))
    recalls_by_year_country.plot(kind='barh', stacked=True, ax=ax, colormap='Set2')
    ax.set_title('Horizontal Bar Chart of Recalls by Year and Top 8 Countries Excluding Canada', color='darkblue')
    ax.set_xlabel('Number of Recalls', color='darkgreen')
    ax.set_ylabel('Country', color='darkred')
    ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left', title_fontsize='13', fontsize='11', facecolor='lightyellow')
    plt.tight_layout()

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

def create_countries_plot_excluding_us_and_canada(df):
    # Convert 'report_date' to datetime to extract the year
    df['report_date'] = pd.to_datetime(df['report_date'], format='%Y%m%d')

    # Extract the year from 'report_date'
    df['report_year'] = df['report_date'].dt.year

    # Exclude both the United States and Canada from the dataframe
    df = df[(df['country'] != 'United States') & (df['country'] != 'Canada')]

    # Group by 'country' to get the total count of recalls and select top 8 countries
    top_countries = df['country'].value_counts().nlargest(8).index

    # Filter the dataframe to include only the top 8 countries
    df_top_countries = df[df['country'].isin(top_countries)]

    # Group by 'report_year' and 'country' to get the count of recalls for top 8 countries
    recalls_by_year_country = df_top_countries.groupby(['report_year', 'country']).size().unstack(fill_value=0)

    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))
    recalls_by_year_country.plot(kind='barh', stacked=True, ax=ax, colormap='Set2')
    ax.set_title('Horizontal Bar Chart of Recalls by Year and Top 8 Countries Excluding US and Canada', color='darkblue')
    ax.set_xlabel('Number of Recalls', color='darkgreen')
    ax.set_ylabel('Country', color='darkred')
    ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left', title_fontsize='13', fontsize='11', facecolor='lightyellow')
    plt.tight_layout()

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

def create_company_distribution_plot(df):
    recalls_by_firm_per_year = df.groupby(['recall_initiation_year', 'recalling_firm']).size().unstack(fill_value=0)

    # Identify the top 8 firms with the most recalls
    top_firms = recalls_by_firm_per_year.sum().nlargest(10).index

    # Filter the data to include only the top 8 firms
    df_top_firms = recalls_by_firm_per_year[top_firms]

    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))
    df_top_firms.plot(kind='barh', stacked=True, ax=ax, colormap='Set2')
    ax.set_title('Horizontal Bar Chart of Recalls by Year and Top 8 Recalling Firms', color='darkblue')
    ax.set_xlabel('Number of Recalls', color='darkgreen')
    ax.set_ylabel('Recalling Firm', color='darkred')
    ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left', title_fontsize='13', fontsize='11', facecolor='lightyellow')
    plt.tight_layout()

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

def create_company_distribution_plot_excluding_top_5_firms(df):
    recalls_by_firm_per_year = df.groupby(['recall_initiation_year', 'recalling_firm']).size().unstack(fill_value=0)

    # Identify the top 20 firms with the most recalls
    top_20_firms = recalls_by_firm_per_year.sum().nlargest(15).index

    # Identify the top 5 firms with the most recalls
    top_5_firms = recalls_by_firm_per_year.sum().nlargest(5).index

    # Exclude the top 5 firms from the top 20
    firms_to_include = top_20_firms.difference(top_5_firms)

    # Filter the data to include only the firms excluding the top 5
    df_excluding_top_5_firms = recalls_by_firm_per_year[firms_to_include]

    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))
    df_excluding_top_5_firms.plot(kind='barh', stacked=True, ax=ax, colormap='Set2')
    ax.set_title('Horizontal Bar Chart of Recalls by Year Excluding Top 5 Recalling Firms', color='darkblue')
    ax.set_xlabel('Number of Recalls', color='darkgreen')
    ax.set_ylabel('Recalling Firm', color='darkred')
    ax.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left', title_fontsize='13', fontsize='11', facecolor='lightyellow')
    plt.tight_layout()

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

def plot_notification_trends(dataframe):
    # Group by 'recall_initiation_year' and 'initial_firm_notification' to count the notifications per year
    notifications_by_year = dataframe.groupby(['recall_initiation_year', 'initial_firm_notification']).size().unstack(fill_value=0)

    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))
    notifications_by_year.plot(kind='line', ax=ax, colormap='Set1', marker='o')
    ax.set_title('Form of Notification Over the Years', fontsize=16, color='darkblue')
    ax.set_xlabel('Year', fontsize=14, color='darkgreen')
    ax.set_ylabel('Number of Notifications', fontsize=14, color='darkred')
    ax.legend(title='Notification Form', bbox_to_anchor=(0.5, -0.2), loc='upper center', title_fontsize='13', fontsize='11', ncol=3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64


def plot_termination_trends(df):
    terminations_by_classification_per_year = df.groupby(['termination_year', 'classification']).size().unstack(fill_value=0)

    plt.figure(figsize=(12, 8))

    # Plot each classification type
    risk_labels = {
        'Class I': 'High Risk Terminations',
        'Class II': 'Mid Risk Terminations'
    }

    for classification in terminations_by_classification_per_year.columns:
        risk_label = risk_labels.get(classification, 'Low Risk Terminations')
        plt.plot(terminations_by_classification_per_year.index, terminations_by_classification_per_year[classification], label=risk_label, marker='o')
    # Add title and labels
    plt.title('Termination Trends by Classification Each Year', fontsize=30)
    plt.xlabel('Year', fontsize=25)
    plt.ylabel('Number of Terminations', fontsize=25)
    plt.grid(True)

    # Add a legend to show the classification types
    plt.legend(fontsize=20)
    
    # Increase the size of the values shown on X and Y axes
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

def plot_recall_trends(df):
    # Group by 'recall_initiation_year' and 'classification' to count the recalls per classification per year
    recalls_by_classification_per_year = df.groupby(['recall_initiation_year', 'classification']).size().unstack(fill_value=0)

    # Plotting the trend of recalls for each classification
    plt.figure(figsize=(12, 8))

    # Plot each classification type
    risk_labels = {
        'Class I': 'High Risk Recalls',
        'Class II': 'Mid Risk Recalls'
    }

    for classification in recalls_by_classification_per_year.columns:
        risk_label = risk_labels.get(classification, 'Low Risk Recalls')
        plt.plot(recalls_by_classification_per_year.index, recalls_by_classification_per_year[classification], label=risk_label, marker='o')

    # Add title and labels with increased font size
    plt.title('Recall Trends by Classification Each Year', fontsize=30)
    plt.xlabel('Year', fontsize=25)
    plt.ylabel('Number of Recalls', fontsize=25)
    plt.grid(True)

    # Add a legend to show the classification types with increased font size
    plt.legend(fontsize=20)
    
    # Increase the size of the values shown on X and Y axes
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64


def plot_termination_duration_distribution(dataframe):
    terminated_recalls = dataframe[dataframe['status'] == 'Terminated']

    # Calculate the mean and median of termination duration
    mean_duration = terminated_recalls['termination_duration_years'].mean()
    median_duration = terminated_recalls['termination_duration_years'].median()

    # Plot the distribution of termination duration
    plt.figure(figsize=(12, 8.5))
    sns.histplot(terminated_recalls['termination_duration_years'], bins=10, kde=True)

    # Add a vertical line at the mean
    plt.axvline(mean_duration, color='red', linestyle='--', label=f'Mean: {mean_duration:.2f} years')

    # Add a vertical line at the median
    plt.axvline(median_duration, color='blue', linestyle='-.', label=f'Median: {median_duration:.2f} years')

    # Annotate the mean
    plt.annotate(f'Mean = {mean_duration:.2f}', 
                 xy=(mean_duration, 0), 
                 xytext=(mean_duration + 1, 3000),  # Adjust text position
                 arrowprops=dict(facecolor='green', shrink=0.05),
                 fontsize=20)

    # Annotate the median
    plt.annotate(f'Median = {median_duration:.2f}', 
                 xy=(median_duration, 100), 
                 xytext=(median_duration + 1, 4000),  # Adjust text position
                 arrowprops=dict(facecolor='yellow', shrink=0.05),
                 fontsize=20)

    # Add labels and title
    plt.title('Distribution of Termination Duration (in Years)\nTrend showing terminations of recall around 1.5 Years', fontsize=25)
    plt.xlabel('Years to Terminate', fontsize=20)
    plt.ylabel('Frequency', fontsize=20)

    # Increase the size of the values shown on X and Y axes
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    # Show the legend
    plt.legend()

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64


def plot_top_5_reasons_for_recall(dataframe):
    recalls_by_reason_per_year = dataframe.groupby(['recall_initiation_year', 'reason_for_recall']).size().unstack(fill_value=1)

    top_5_reasons = recalls_by_reason_per_year.sum().nlargest(5).index

    top_5_recalls_by_reason_per_year = recalls_by_reason_per_year[top_5_reasons]

    plt.figure(figsize=(16, 8))
    top_5_recalls_by_reason_per_year.plot(kind='barh', stacked=True, color=['#8B0000', '#FF8C00', '#4682B4', '#006400', '#FFD700'], ax=plt.gca())

    # Add title and labels
    plt.title('Top 5 Reasons for Drug Recalls Each Year', fontsize=30)
    plt.xlabel('Number of Recalls', fontsize=20)
    plt.ylabel('Year', fontsize=20)
    plt.grid(axis='x')

    # Add a legend to show the reasons for recall
    plt.legend(title='Reason for Recall', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=15)

    plt.text(
        1.1, 
        0.4, 
        """Not much recall data is available 
        \nbefore 2011 to understand any trend.
        \nBiggest reason for recall is 
        \nLack of Assurance of Sterility
        \nEven though we have other reasons
        \n causing to skew the trend""", 
         transform=plt.gca().transAxes, fontsize=20, verticalalignment='center', horizontalalignment='left')

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64

def create_line_plot(dataframe, variation):
    if variation == "termination":
        return plot_termination_trends(df = dataframe)
    elif variation == "recall":
        return plot_recall_trends(dataframe)

def update_line_plot(selected_risk_level, dataframe):
    return create_line_plot(variation=selected_risk_level, dataframe=dataframe)