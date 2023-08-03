from transformers import pipeline

model_name = "facebook/nllb-200-1.3B"
pipe = pipeline("translation", model=model_name)

def translate_bulk(texts, source_lang, target_lang):
    res = pipe(texts, src_lang=source_lang, tgt_lang=target_lang)
    return [r['translation_text'] for r in res]

