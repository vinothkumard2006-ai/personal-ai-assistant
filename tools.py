import wikipedia

def search_tool(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return "No result found"

def calculator_tool(query):
    try:
        return str(eval(query))
    except:
        return "Calculation error"