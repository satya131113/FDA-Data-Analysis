from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from plots import create_company_distribution_plot, create_company_distribution_plot_excluding_top_5_firms, create_countries_plot, create_countries_plot_excluding_canada, create_countries_plot_excluding_us, create_countries_plot_excluding_us_and_canada, plot_notification_trends, plot_termination_duration_distribution, plot_top_5_reasons_for_recall, update_line_plot

def create_header():
    return html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '0px'}, children=[
        html.H1(children='FDA Data Analysis', style={'textAlign': 'center', 'color': '#007aff', 'fontWeight': 'bold'})
    ])

def create_dashboard_title():
    return html.Div(id='dashboard-title', style={'fontFamily': 'Arial, sans-serif', 'padding': '0px'}, children=[
        html.H3(id='dashboard-title-text', style={'textAlign': 'center', 'color': '#8e8e93'})
    ])

@callback(
    Output('dashboard-title-text', 'children'),
    Input('tabs', 'value')
)
def update_dashboard_title(selected_tab):
    if selected_tab == 'drug_recall_report':
        return 'Data Analysis of Drug Recall from 2006-2024'
    elif selected_tab == 'drug_risk_termination_trend':
        return 'Drug Risk Level and Recall Termination Trend'
    elif selected_tab == 'reason_notify_trend':
        return 'Drug Recall Reasons and Intial Notication to Firm Trends'
    elif selected_tab == 'country_firm_trend':
        return 'Country and Firm Level Trends'
    else:
        return 'FDA Data Analysis'

def create_tab_1(dataframe):
    ## Data Descriptions and Insights section
    children_components = [
        html.Div(style={'display': 'flex', 'justifyContent': 'center', 'padding': '10px'},children=[
            html.Div(children=[
                html.P("The data is collected from the official site of FDA. It contains data on drug recalls from 2006 to 2024. The analysis focused on drugs recall trends over the year and drug recall termination.Multiple variation like country, risk level of the recalled drug (The classification of recalls indicates the health hazard level posed by the product,Class I: serious risk or death, Class II: reversible risk, Class III: unlikely risk), recalling firm and the way the firm initiaally got notified are explored here. The exploration over timeseries data revealed some interesting insights. Here are some findings", style={'color': '#000000', 'fontWeight': 'bold'}),
                html.Ul(children=[
                    html.Li("Most recalled drugs of Class II - Mid level risk with reversible risk.One notable change in trend is after 2017 when a large number of Class I drugs are recalled."),
                    html.Li("For a recalled drug to get termination on the recall in takes about 20 months in general. A concerning observation is when a huge number of Class I drugs got termination on recall, at this point it even crossed the Class II drugs termination recall count."),
                    html.Li("Max drug recall from United States is something expected as the data is form FDA, but we exclude US and check we see Canada, China and India as some countries from where the drugs were recalled most, but still 2015 presents as skew with Canada. Excluding Canada too it becomes clear countries Mexico, Germany, Jordan also have drug recalls by FDA."),
                    html.Li("One funny thing is the trend for initially notifying the firm about a drug recall is thorugh a letter instead of faster alternative like Email or FAX or Telephone."),
                    html.Li(html.A("FDA Data Source", href="https://open.fda.gov/data/downloads", target="_blank", style={'color': '#007aff'}))
                ], style={'textAlign': 'left', 'color': '#000000', 'padding': '10px'})
            ], style={'display': 'block'})
        ])        
    ]

    total_recalls = len(dataframe)
    active_recalls = len(dataframe[dataframe['status'] == 'Ongoing'])
    terminated_recalls = len(dataframe[dataframe['status'] == 'Terminated'])
    average_recall_termination_duration = round(dataframe['days_to_termination'].mean(skipna=True), 2)


    recalls_by_classification = dataframe['classification'].value_counts().to_dict()
    recalls_by_reason = dataframe['reason_for_recall'].value_counts().to_dict()
    top_recalling_firms = dataframe['recalling_firm'].value_counts().head(5).to_dict()
    top_initial_firm_notifications = dataframe['initial_firm_notification'].value_counts().head(10).to_dict()

    stat_cards = html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'}, children=[
        html.Div(style={'backgroundColor': '#f8f9fa', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4('Total Recalls', style={'color': '#007aff'}),
            html.P(total_recalls, style={'fontSize': '20px', 'fontWeight': 'bold'})
        ]),
        html.Div(style={'backgroundColor': '#f8f9fa', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4('Active Recalls', style={'color': '#007aff'}),
            html.P(active_recalls, style={'fontSize': '20px', 'fontWeight': 'bold'})
        ]),
        html.Div(style={'backgroundColor': '#f8f9fa', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4(['Terminated', html.Br(), 'Recalls'], style={'color': '#007aff'}),
            html.P(terminated_recalls, style={'fontSize': '20px', 'fontWeight': 'bold'})
        ]),
        html.Div(style={'backgroundColor': '#f8f9fa', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4(['Average Recall', html.Br(), 'Termination Duration'], 
                    style={'color': '#007aff'}),
            html.P(f"{average_recall_termination_duration} days", style={'fontSize': '20px', 'fontWeight': 'bold'})
        ]),
        html.Div(style={'backgroundColor': '#f8d7da', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4('Class I', style={'color': '#721c24'}),
            html.H4('High Risk', style={'color': '#721c24'}),
            html.P(f"{recalls_by_classification.get('Class I', 0)}", style={'fontSize': '20px', 'fontWeight': 'bold'})
        ]),
        html.Div(style={'backgroundColor': '#fff3cd', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4('Class II', style={'color': '#721c24'}),
            html.H4('Medium Risk', style={'color': '#856404'}),
            html.P(f"{recalls_by_classification.get('Class II', 0)}", style={'fontSize': '20px', 'fontWeight': 'bold'})
        ]),
        html.Div(style={'backgroundColor': '#d4edda', 'padding': '10px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4('Class III', style={'color': '#721c24'}),
            html.H4('Low Risk', style={'color': '#155724'}),
            html.P(f"{recalls_by_classification.get('Class III', 0)}", style={'fontSize': '20px', 'fontWeight': 'bold'})
        ]),
    ])

    children_components.append(stat_cards)

    # Create cards for classification risks and top reasons for recall in a single row
    classification_risk_and_top_info_cards = html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'padding': '20px'}, children=[
        html.Div(style={'backgroundColor': '#e0f7fa', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4('Top Reasons for Recall', style={'color': '#007aff'}),
            html.P(''.join([f"{reason} ({count})\n" for reason, count in sorted(recalls_by_reason.items(), key=lambda x: x[1], reverse=True)[:5]]).strip(), style={'fontSize': '16px', 'whiteSpace': 'pre-line'})
        ]),
        html.Div(style={'backgroundColor': '#e8f5e9', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4('Top Recalling Firms', style={'color': '#388e3c'}),
            html.P(''.join([f"{firm} ({count})\n" for firm, count in top_recalling_firms.items()]).strip(), style={'fontSize': '16px', 'whiteSpace': 'pre-line'})
        ]),
        html.Div(style={'backgroundColor': '#e8f5e9', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'textAlign': 'center'}, children=[
            html.H4('Ways to Notify Firms', style={'color': '#388e3c'}),
            html.P(''.join([f"{notification} ({count})\n" for notification, count in top_initial_firm_notifications.items()]).strip(), style={'fontSize': '16px', 'whiteSpace': 'pre-line'})
        ])
    ])

    children_components.append(classification_risk_and_top_info_cards)

    return dcc.Tab(
        label='Drug Recall Report', 
        value='drug_recall_report', 
        children=children_components, 
        selected_style={
            'borderRadius': '20px', 
            'backgroundColor': '#007aff', 
            'color': '#ffffff', 
            'padding': '10px', 'margin': '5px'
        }, 
        style={
            'borderRadius': '15px', 
            'backgroundColor': '#ffffff', 
            'color': '#000000', 
            'padding': '10px', 
            'margin': '5px'
        }
    )

def create_tab_2(dataframe):
    children_components = []
    line_plot_children = []
    selected_risk_level_dropdown_left = dcc.Dropdown(
        id='risk-level-dropdown',
        options=[
            {'label': 'Recall', 'value': 'recall'},
            {'label': 'Termination', 'value': 'termination'}
        ],
        value='recall',  # Default value
        clearable=False,
        style={'width': '100%'}  # Ensure the dropdown occupies the full width of its container
    )
    line_plot_children.append(html.Div(style={'padding': '10px', 'display': 'flex', 'justifyContent': 'flex-start', 'width': '90%'}, children=[selected_risk_level_dropdown_left]))

    @callback(
        Output('line-plot-image', 'src'),
        Input('risk-level-dropdown', 'value')
    )
    def update_selected_risk_level_left(selected_risk_level):
        image_base64_2 = update_line_plot(selected_risk_level, dataframe)
        return 'data:image/png;base64,{}'.format(image_base64_2)

    line_plot_children.append(html.Div(style={'padding': '10px', 'display': 'flex', 'justifyContent': 'flex-start', 'width': '90%'}, children=[
        html.Img(id='line-plot-image', style={'width': '100%', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'})
    ]))

    # Trend time years for termination
    termination_duration_distribution_plot = plot_termination_duration_distribution(dataframe)  # Assuming you want to use the same plot function for demonstration

    children_components.append(html.Div(style={'display': 'flex', 'justifyContent': 'space-between'}, children=[
        html.Div(style={'width': '50%'}, children=line_plot_children),
        html.Div(style={'width': '50%'}, children=[
            html.Img(src='data:image/png;base64,{}'.format(termination_duration_distribution_plot), style={'width': '100%', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'})
        ])
    ]))
    children_components.append(html.Hr(style={'border': '1px solid #ccc', 'width': '100%'}))
    return dcc.Tab(
        label='Risk Level',
        value='drug_risk_termination_trend',
        children=children_components,
        selected_style={
            'borderRadius': '20px',
            'backgroundColor': '#007aff',
            'color': '#ffffff',
            'padding': '10px',
            'margin': '5px'
        },
        style={
            'borderRadius': '15px',
            'backgroundColor': '#ffffff',
            'color': '#000000',
            'padding': '10px',
            'margin': '5px'
        }
    )

def create_tab_3(dataframe):
    children_components = []
    recall_reasons_trend_plot = plot_top_5_reasons_for_recall(dataframe=dataframe)
    component_3 = html.Div(style={'display': 'flex', 'justifyContent': 'center', 'padding': '10px'}, children=[
        html.Img(src='data:image/png;base64,{}'.format(recall_reasons_trend_plot), style={'width': '80%', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'})
    ])
    children_components.append(component_3)

    firms_notification_mechanism_plot = plot_notification_trends(dataframe=dataframe)
    component_5 = html.Div(style={'display': 'flex', 'justifyContent': 'center', 'padding': '10px'}, children=[
        html.Img(src='data:image/png;base64,{}'.format(firms_notification_mechanism_plot), style={'width': '80%', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'})
    ])
    children_components.append(component_5)
    return dcc.Tab(
        label='Reason and Notification',
        value='reason_notify_trend',
        children=children_components,
        selected_style={
            'borderRadius': '20px',
            'backgroundColor': '#007aff',
            'color': '#ffffff',
            'padding': '10px',
            'margin': '5px'
        },
        style={
            'borderRadius': '15px',
            'backgroundColor': '#ffffff',
            'color': '#000000',
            'padding': '10px',
            'margin': '5px'
        }
    )


def create_tab_4(dataframe):
    children_components = []
    # Add a dropdown to select plot type: by country or by company
    plot_type_dropdown = dcc.Dropdown(
        id='plot-type-dropdown',
        options=[
            {'label': 'By Country', 'value': 'country'},
            {'label': 'By Company', 'value': 'company'}
        ],
        value='company',  # Default to company-wise plot
        clearable=False,
        style={'fontSize': '20px', 'width': '40%'}  # Increase the font size and ensure full width
    )
    children_components.append(plot_type_dropdown)

    # Add a checkbox to include or exclude the USA and Canada in the plot
    include_countries_checklist = dcc.Checklist(
        id='include-countries-checklist',
        options=[
            {'label': 'Include USA', 'value': 'include_usa'},
            {'label': 'Include CANADA', 'value': 'include_canada'}
        ],
        value=['include_usa', 'include_canada'],  # Default to including both USA and Canada
        style={'fontSize': '20px'}  # Increase the font size of the checkbox text
    )
    children_components.append(include_countries_checklist)

    # Add a checkbox to include or exclude the top 5 firms in the company plot
    include_top_5_firms_checklist = dcc.Checklist(
        id='include-top-5-firms-checklist',
        options=[
            {'label': 'Include Top 5 Firms', 'value': 'include_top_5'}
        ],
        value=['include_top_5'],  # Default to including top 5 firms
        style={'fontSize': '20px'}  # Increase the font size of the checkbox text
    )
    children_components.append(include_top_5_firms_checklist)

    @callback(
        Output('country-wise-recall-image', 'src'),
        Output('include-countries-checklist', 'style'),
        Output('include-top-5-firms-checklist', 'style'),
        Input('plot-type-dropdown', 'value'),
        Input('include-countries-checklist', 'value'),
        Input('include-top-5-firms-checklist', 'value')
    )
    def update_recall_plot(plot_type, selected_countries, selected_firms):
        if plot_type == 'country':
            # Show the checklist when country plot is selected
            checklist_style = {'display': 'block', 'fontSize': '20px'}
            firms_checklist_style = {'display': 'none'}
            if 'include_usa' in selected_countries and 'include_canada' in selected_countries:
                image_base64 = create_countries_plot(dataframe)
            elif 'include_usa' in selected_countries:
                image_base64 = create_countries_plot_excluding_canada(dataframe)
            elif 'include_canada' in selected_countries:
                image_base64 = create_countries_plot_excluding_us(dataframe)
            else:
                image_base64 = create_countries_plot_excluding_us_and_canada(dataframe)
        else:
            # Hide the country checklist and show the firms checklist when company plot is selected
            checklist_style = {'display': 'none'}
            firms_checklist_style = {'display': 'block', 'fontSize': '20px'}
            if 'include_top_5' in selected_firms:
                image_base64 = create_company_distribution_plot(dataframe)
            else:
                image_base64 = create_company_distribution_plot_excluding_top_5_firms(dataframe)

        return 'data:image/png;base64,{}'.format(image_base64), checklist_style, firms_checklist_style

    # Update the component to use the callback output
    component_4 = html.Div(style={'display': 'flex', 'justifyContent': 'center', 'padding': '10px'}, children=[
        html.Img(id='country-wise-recall-image', style={'width': '80%', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'})
    ])
    children_components.append(component_4)

    return dcc.Tab(
        label='Country and Firm Level',
        value='country_firm_trend',
        children=children_components,
        selected_style={
            'borderRadius': '20px',
            'backgroundColor': '#007aff',
            'color': '#ffffff',
            'padding': '10px',
            'margin': '5px'
        },
        style={
            'borderRadius': '15px',
            'backgroundColor': '#ffffff',
            'color': '#000000',
            'padding': '10px',
            'margin': '5px'
        }
    )

def create_layout(dataframe):
    image_base64_2 = create_countries_plot(dataframe)

    return html.Div(children=[
        create_header(),
        create_dashboard_title(),
        dcc.Tabs(
            id='tabs',
            value='drug_recall_report',
            vertical=True,
            colors={
                'border': '#d1d1d6',
                'primary': '#007aff',
                'background': '#f8f8f8'
            },
            children=[
                create_tab_1(dataframe=dataframe),
                create_tab_2(dataframe=dataframe),
                create_tab_3(dataframe=dataframe),
                create_tab_4(dataframe=dataframe)
            ],
            style={
                'padding': '10px',
                'width': '200px',  # Set a fixed width for the tabs bar
                'minWidth': '200px',  # Ensure the minimum width is consistent
                'maxWidth': '200px'  # Ensure the maximum width is consistent
            }
        )
    ])