# URL categorization
Internet can be used as one important source of information for machine learning algorithms. Web pages store diverse information about multiple domains. One critical problem is how to categorize this information.

Websites classification is performed by using NLP techniques that helps to generate words frequencies for each category and by calculating categories weights it is possible to predict categories for Websites.

This repository is made for a challenge that Adot proposes, we are going to train a neural network to predict the categories of each given URL (even if this URL does not exist in reality, so we are not going to scrape the content of the pages which could give very good results) but we are going to use the URLs only.

The Dataset is given by the company in the format of several parquet files and it contains 3 columns:

*   URLs (Uniform Resource Locator): pages and web sites identifiers
*   Targets: the list of classes associated to the url ← what we want to predict
*   Day: day of the month

## Follow-up process
Multi-label classification is not an easy task especially with a dataset that requires a lot of manipulation before being ready for training, the following notebook shows the approach followed and the choices taken for training the model.  [URL categorization Colab](https://colab.research.google.com/drive/1w4GOV9h2pPI9P-E8Z-Z2qzsrQVduVzFS?usp=sharing) .

## Usage

If you want to use my complete solution (my pre-trained model with the interface), you can launch directly docker compose which retrieves the images (already uploaded on docker hub) with the following command:
```console
pika@pika:~$ docker-compose ....
```
