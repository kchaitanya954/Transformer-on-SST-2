# Transformer-on-SST-2

## 1. Install dependencies
```bash
pip install -r requirements.txt
```

## Training loss for each batch and accuracy for train and dev datasets for 10 epochs
![alt text](https://github.com/kchaitanya954/Transformer-on-SST-2/blob/main/images/plot.png?raw=true)

## Information about the model
* The time complexity of my solution would primarily depend on the complexity of the BertModel used in the EfficientTransformer class. The BertModel is a transformer-based model that uses self-attention mechanisms to process the input data. The time complexity of self-attention mechanisms is O(n^2), where n is the number of tokens in the input sequence. Additionally, the solution includes an LSTM layer, which has a time complexity of O(n) for a single layer. Finally, the solution includes a linear layer and a dropout layer, both of which have a time complexity of O(n). Therefore, the overall time complexity of the solution would be O(n^2) for the BertModel and O(n) for the LSTM, linear, and dropout layers.

* The memory complexity of the solution would depend on the number of parameters in the BertModel and the LSTM, linear, and dropout layers. The model has total The model has 723,457 trainable parameters.

## Parts of the architecture correspond to the pefrormance (time / memory complexity)
* We are freezing its parameters during training. This reduces the number of parameters that need to be updated during training, and therefore reduces the time and memory required for training.
* Using a single-layer LSTM instead of multiple layers. Each additional layer in a RNN increases the time and memory complexity of the model.
* Using a linear layer (nn.Linear) with a hidden dimension of 256 instead of the original hidden size of the transformer model. This reduces the number of parameters in the model, leading to faster training and less memory usage.
* Using dropout layers (nn.Dropout) to regularize the model and prevent overfitting. This can also help to reduce the number of parameters in the model, leading to faster training and less memory usage.

## Comapring to vanilla architecture of the Transformer.
* The solution that we have used here adds a linear reshape layer, a LSTM layer, and a linear layer on top of the pre-trained transformer model. These additional layers increase the model's capacity to learn the input data, which can potentially lead to improved performance. However, these added layers also increase the overall time and memory complexity of the model, as they require additional computation during both the forward and backward passes. We also added a dropout layer, which can help to reduce overfitting by randomly dropping out some of the activations during training.

* In terms of the vanilla architecture of the transformer, the solution modifies the architecture by adding layers on top of the pre-trained transformer model. This can potentially lead to improved performance on the task at hand but also can increases the time and memory complexity of the model.

## Description of the chosen tasks: brief overview, metrics and SOTA;
* In this task, we are trying to create an efficient transformer model by modifying the architecture of the vanilla transformer model. The goal was to improve the performance of the model in terms of time and memory complexity. This was achieved by adding or removing layers from the original architecture, and by modifying the existing layers.

* The metrics used to evaluate the performance of the model are accuracy and loss. The accuracy is measured by comparing the predicted outputs of the model to the actual outputs, and calculating the percentage of correctly predicted outputs. The loss is calculated as the difference between the predicted outputs and the actual outputs. The lower the loss, the better the performance of the model.

* The accuracy of the model for 10 epochs on test data is around 81%, which can be furether increased by increasing the num of epochs, and tuning the parameters of the model.

* The Reference task accuracy (vanilla Transformer) is around 90%.

Latency benchmarks: It takes arounf 30 sec for one iteration of batch size 128, and number of batches are 55. and the model has 723,457 trainable parameters

