import pandas as pd
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from langchain_community.document_loaders import WebBaseLoader

# Read URLs from the CSV file
name = 'results-v2.2.0'
csv_file_path = f'{name}.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)

# Initialize the metric
answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.7, strict_mode=True)

# List to store results
results = []

# Iterate over each URL in the CSV
for index, row in df.iterrows():
    url = row['URL']
    actual_output = row['output']
    loader = WebBaseLoader(url)
    data = loader.load()[0].page_content
    context = ' '.join(data.split())

    # Define the test case
    test_case = LLMTestCase(
        input=f"",
        # Replace this with the actual output from your LLM application
        actual_output=f'{actual_output}'
    )

    answer_relevancy_metric.measure(test_case)
    score = answer_relevancy_metric.score
    reason = answer_relevancy_metric.reason
  

    # Append the result to the list
    results.append({'url': url, 'output': actual_output, 'score': score, 'reason': reason})

# Convert the results list to a DataFrame
results_df = pd.DataFrame(results)

# Save the results to a new CSV file
output_csv_file_path = f'{name}(with_scores).csv'  # Replace with your desired output file path
results_df.to_csv(output_csv_file_path, index=False)


print(f'Results saved to {output_csv_file_path}')
