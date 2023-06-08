from Nuggt_Playground import *
from sidebar_functions import sidebar_logo

st.set_page_config(page_title="Financial Data Display", layout="wide")

sidebar_logo("nuggt-logo.png")

st.subheader("Financial Data Display")

user_input = """Step: Open {upload:file} using {tool:python}
Step: Display its description using {tool:python}
Step: Complete the task {text:input} using {tool:python}
Step: Display your results using {tool:display}
"""
output_format = "ack"

# st.markdown("""Upload an Excel/CSV file for data analysis. You can ask the app generic questions like "summarise this data" or specific questions like "What is the relationship between Column A and Column B". The app can also generate data visualisations like bargraphs, piecharts etc. You can generate visualisations by typing "Generate visualisations for.." 
# """)
# st.markdown("""This app was created with a single AI command - 
#             **Open :red[{upload : file}] using :green[{tool : document_loader}] and complete the task :blue[{text : input}] using :green[{tool : data_analysis}]**  \n
# """)
# st.markdown("""**- :red[file]** is a variable that defines your input file.
# """)
# st.markdown("""**- :green[document_loader]** is a tool used for the loading uploaded documents.
# """)
# st.markdown("""**- :blue[input]** is a variable that defines your input query.
# """)
# st.markdown("""**- :green[data_analysis]** is a tool that does the data analysis on your input file.
# """)

if user_input and output_format:
    save_to_sheets(user_input, output_format, "-", "-")
    variables = extract_variables(user_input)
    nuggt(user_input, output_format, variables)












