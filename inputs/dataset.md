Para geração do dataset utilizado para a previsão de vendas, foi solicitado ao Deepseek que gerasse um dataset com as características desejadas através do seguinte prompt:

*Prompt*: Create a dataset of 3*365 (three years of data) records of ice creams sales, with 3 different cone sizes, 2 flavors, real dates (so we can differentiate weekday from weekends) 
and average temperature for the day, for the city of Rio de Janeiro. The correlation between all variables must correspond to expected real-world market sales (e.g.: higher temperature 
should, usually, correlate with higher sales, all things being equal). Generate this dataset as a csv file.

Como resposta, o Deepseek gerou o script python dataset_vendas.py com as correlações pré-estabelecidas para geração desse dataset, de forma que possamos saber se o modelo de predição desse dataset corresponde 
ao modelo gerador do dataset.
