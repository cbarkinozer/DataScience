from datasets import load_dataset, DatasetDict
import os

def load_and_return_dataset():
  """Loads the OpenAssistant oasst2 dataset and returns it.

  This function does not take any arguments, as it downloads the dataset
  directly within its implementation.

  Returns:
    The loaded datasets.Dataset object.
  """
  dataset = load_dataset("OpenAssistant/oasst1", cache_dir="./data2")
  return dataset

def filter(dataset):
  """Filters the dataset to keep only rows where the `lang` feature is 'tr'.
  Args:
    dataset: The DatasetDict object to filter.

  Returns:
    The filtered DatasetDict object.
  """
  filtered_dataset = DatasetDict({
      split: dataset[split].filter(lambda example: example["lang"] == "tr")
      for split in dataset.keys()
  })
  return filtered_dataset

def save_as_csv(filtered_dataset, output_dir="./output2"):
  """Saves each split of the DatasetDict as a separate CSV file.

  Args:
    filtered_dataset: The DatasetDict to save.
    output_dir (str, optional): The directory to save the CSV files in. Defaults to "./output_csv".
  """

  os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

  for split, dataset in filtered_dataset.items():
    csv_path = os.path.join(output_dir, f"{split}.csv")
    dataset.to_csv(csv_path)

  print(f"Filtered dataset saved as CSV files in: {output_dir}")

if __name__ == "__main__":
  dataset = load_and_return_dataset()
  print(dataset) 
  '''
  DatasetDict({
    train: Dataset({
        features: ['message_id', 'parent_id', 'user_id', 'created_date', 'text', 'role', 'lang', 'review_count', 'review_result', 'deleted', 'rank', 'synthetic', 'model_name', 'detoxify', 'message_tree_id', 'tree_state', 'emojis', 'labels'],
        num_rows: 128575
    })
    validation: Dataset({
        features: ['message_id', 'parent_id', 'user_id', 'created_date', 'text', 'role', 'lang', 'review_count', 'review_result', 'deleted', 'rank', 'synthetic', 'model_name', 'detoxify', 'message_tree_id', 'tree_state', 'emojis', 'labels'],
        num_rows: 6599
    })
})
  '''
  filtered_dataset = filter(dataset)
  save_as_csv(filtered_dataset)
