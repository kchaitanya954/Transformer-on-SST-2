from transformers import BertModel
import torch.nn as nn

class EfficientTransformer(nn.Module):
    def __init__(self,checkpoint,hidden_dim, dropout_rate: float = 0.1):
        super().__init__()
        self.mybert=BertModel.from_pretrained(checkpoint)
        for param in self.mybert.parameters():
            param.requires_grad = False
        self.reshape = nn.Linear(self.mybert.config.hidden_size, hidden_dim)
        self.rnn_lstm = nn.LSTM(hidden_dim, hidden_dim, num_layers=1, batch_first=True)
        self.fc= nn.Linear(hidden_dim,1)
        self.dropout = nn.Dropout(dropout_rate)
        self.activation=nn.Sigmoid()
        
    def forward(self, input_ids,attention_mask):
        bert_output=self.mybert(input_ids = input_ids,attention_mask =attention_mask)
        
        x = self.dropout(bert_output[0])
        x = self.reshape(x)
        lstm_out,(hiden,cell)=self.rnn_lstm(x)
        hiden=torch.squeeze(hiden)
        fc_out=self.fc(hiden)
        final_out=self.activation(fc_out)
        return final_out
