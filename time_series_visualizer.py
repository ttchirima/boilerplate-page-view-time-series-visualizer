import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])


# Clean data
df = df[(df.value > df.value.quantile(0.025)) & (df.value < df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    df.plot(ax=ax, kind='line', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%b')
    df_bar = df_bar.groupby(['year', 'month']).mean().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots()
    sns.barplot(data=df_bar, x='year', y='value', hue='month', ax=ax)
    ax.legend(title='Months')
    ax.set_title('Average Daily Page Views for Each Month Grouped by Year')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Years')
    ax[0].set_ylabel('Page Views')
    sns.boxplot(data=df_box, x='month', y='value', ax=ax[1])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Months')
    ax[1].set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
