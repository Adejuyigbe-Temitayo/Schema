class SchemeMyMessage:

    def read_and_clean(self, input_filepath):
        df = pd.read_json(input_filepath)
        message = df.loc[:, 'message']
        clean_message_data = pd.DataFrame(message.dropna())
        clean_message_data.to_dict()
        return clean_message_data

    def type_map(self, element):
        if type(element) == str:
            message = "String"
        elif type(element) == int:
            message = "Integer"
        elif type(element) == float:
            message = "Float"
        elif type(element) == bool:
            message = "Boolean"
        elif type(element) == list and element is not None and [type(element[i]) == str for i in range(len(element)-1)]:
            message = "Enum"
        elif type(element) == list and element is not None and [type(element[i]) == dict for i in range(len(element)-1)]:
            message = "Array"
        elif type(element) == list:
            message = "List"
        elif type(element) == tuple:
            message = "Tuple"
        elif type(element) == dict:
            message = "Dictionary"
        else:
            message = "Other Lists type"
        return message

    def schema_function(self, file_path):
        clean_message_data = self.read_and_clean(file_path)
        schema = {}
        for index, values in clean_message_data.iterrows():
            for value in values:
                info = {
                    "type": self.type_map(value),
                    "tag": "",
                    "description": f"This gives information about the {index}",
                    "required": 'false'}
                schema[index] = info
        return schema

    def writing_output(self, schema, output_filepath):
        with open(output_filepath, "w") as output_file:
            output_file.write(json.dumps(schema, indent=4))
            
