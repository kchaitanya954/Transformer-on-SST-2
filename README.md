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
