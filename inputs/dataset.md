Para geração do dataset utilizado para a previsão de vendas, foi solicitado ao Deepseek que gerasse um dataset com as características desejadas através do seguinte prompt:

**Prompt Input**: Create a dataset of 3*365 (three years of data) records of ice creams sales, with 3 different cone sizes, 2 flavors, real dates (so we can differentiate weekday from weekends) 
and average temperature for the day, for the city of Rio de Janeiro. The correlation between all variables must correspond to expected real-world market sales (e.g.: higher temperature 
should, usually, correlate with higher sales, all things being equal). Generate this dataset as a csv file.

Como resposta, o Deepseek gerou o script python dataset_vendas.py com as correlações pré-estabelecidas para geração desse dataset, de forma que possamos saber se o modelo de predição desse dataset corresponde 
ao modelo gerador do dataset.

**Prompt Output**: This script generates a realistic dataset with the following characteristics:

Key Features:

    3 years of daily data (2021-2023)

    3 cone sizes: Small, Medium, Large

    2 flavors: Chocolate, Strawberry

    Real dates with weekday/weekend differentiation

    Realistic Rio de Janeiro temperatures (15-40°C range)

    Market-realistic correlations

Realistic Sales Patterns:

    Temperature correlation: Higher temperatures generally increase sales, with optimal sales around 30°C

    Weekend effect: 50% higher sales on weekends

    Seasonal patterns: Higher sales in summer months (Dec-Feb)

    Holiday boosts: Significant sales increases during Carnival and New Year periods

    Size preferences: More large cones sold on hotter days

    Flavor preferences: Chocolate is more popular than strawberry

Expected Correlations:

    Positive correlation between temperature and sales

    Positive correlation between weekend and sales

    Seasonal patterns aligned with Rio's climate

    Realistic distribution across product combinations

The dataset will be saved as rio_ice_cream_sales.csv with the following columns:

    date, day_of_week, is_weekend, cone_size, flavor, temperature, daily_sales
