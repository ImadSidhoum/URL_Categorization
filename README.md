# URLs Categorization
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

*   If you want to use my complete solution (my pre-trained model with the interface), you can use docker-compose which retrieves all my images (already uploaded on docker hub) with the following command:

        docker-compose up


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After the docker-compose finishes downloading the images and running them, you can find the interface in port 3000 [Interface](http://localhost:3000/).



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You should give the URL in the corresponding box and press the send button, the content of the page will be displayed and the categories of the page will appear at the bottom.

*  If you want to use the pre-trained model only (as API), you can download the image from docker hub with the following command:

        docker run -p 5001:5001 dami7/url_maestro:0.2

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;That will launch an API that runs in port 5001. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To make predictions you have to pass a list of strings (URLs) in POST to port 5001 and you receive a list of categories (for each passed URL you receive a list of categories), a simple example is given in the example folder to guide you.

*    If you want to re-train the model, you can use the notebook where you can change the dataset, the hyperparameters .... the code is made in a generic way so that it works if you just change the inputs. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You will need to open an account at [Wandb](https://wandb.ai/), if you want to keep track of your experiments (all the metrics you want: loss, accuracies, hyperparameters, models, system information like the name of GPU used, execution time, memory used, energy consumption .....  ) and even to compare between experiments.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The folder 'artifatcs' must contain the model and the json file (of label encoder).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Once the model is ready, it's time to build the docker image with the following command: 

        docker build -t url_maestro .

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then run the API with the following command:

        docker run -p 5001:5001 url_maestro



