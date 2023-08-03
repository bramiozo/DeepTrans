'''
Utils: contains
    - load_glossary: load glossary from Google cloud or from disk
    - cost_estimator: estimate cost of translation
    - upload_glossary: upload glossary to Google cloud
    - clean_text: clean text
    - de-identify: deanonymize text
    - de-abbreviate: de-abbreviate text
'''

def cost_estimator(texts, model_name):
    '''
    Estimate cost of translation
    '''

    # Get number of characters
    num_chars = sum([len(t) for t in texts])

    cost_per_char = Config['model_name']['cost_per_char']