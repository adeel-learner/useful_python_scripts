from transformers import pipeline
import logging

# Set the logging level for the Transformers library to suppress unnecessary logs
logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)

# Create a pipeline for the masked language modeling task using the BERT model
unmasker = pipeline('fill-mask', model='bert-base-uncased')

# Use the pipeline to predict and fill in the masked token in the given sentence
result = unmasker("The boy is a [MASK].")

# Print the predicted results
for prediction in result:
    print(prediction['token_str'], prediction['score'])
