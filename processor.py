import openai
import xlwings as xw
from xlwings_handler import get_openai_key

def process_excel_data(input_column, output_column):
    # Process questions in the input column and populate answers in the output column.
    api_key = get_openai_key()
    if not api_key:
        return "API key not found. Please set up the API key first."

    openai.api_key = api_key

    try:
        wb = xw.Book.caller()
        sheet = wb.sheets.active
        input_values = sheet.range(f"{input_column}1:{input_column}").value

        if not input_values:
            return "Input column is empty."

        output_values = []
        for question in input_values:
            if question:
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=question,
                    max_tokens=50,
                )
                output_values.append(response.choices[0].text.strip())
            else:
                output_values.append(None)

        sheet.range(f"{output_column}1").value = [[v] for v in output_values]
        return "Processing complete."

    except Exception as e:
        return f"Error processing Excel data: {e}"
