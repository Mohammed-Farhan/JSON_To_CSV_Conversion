import os
import pandas as pd

class JSONToCSV:
	"""An object that can convert multiple JSON files to a CSV file."""
	def __init__(self, source_path, destination_path):
		"""
		Initialize object's attributes.
		:parameter str source_path: Path to JSON files.
		:parameter str destination_path: Output path.
		"""
		self.source_path =  '../JSON_Conversion/'
		self.destination_path ='../output.csv'
		 

	def convert_json_to_csv(self):
		"""Converting multiple JSON files to a CSV file"""
		list_df = []
		for file in os.listdir(self.source_path):
			if file.endswith('.json'):
				print(file)
				source_file_path = self.source_path + file
				df = pd.read_json(source_file_path)
				print(df)
				list_df.append(df)
		all_df = pd.concat(list_df)
		print(all_df)
		headerList =["Names", "Person's Age", "Gender"]
		all_df.to_csv('output.csv',sep='\t',header=headerList, encoding='utf-8',index=False)
		print("All JSON files in {} are successfully converted into a CSV "
			  "file named {}".format(self.source_path, self.destination_path))

if __name__ == '__main__':
	json_path = '../JSON_Conversion/*.json' # Path to JSON files
	output_path =  '../output.csv'  # Output path

	converter = JSONToCSV(json_path, output_path)
	converter.convert_json_to_csv()


