from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM


class PredictorEngine:

    def __init__(self, model_type: str = 'Codegen2_1'):
        self.model = self.__get_model(model_type)
        self.device = "cpu"

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.model, load_in_4bit=True)
        model = AutoModelForCausalLM.from_pretrained(self.model, trust_remote_code=True, revision="main").to(self.device)

        input_ids = tokenizer(text, return_tensors="pt").input_ids
        generated_ids = model.generate(input_ids, max_length=128, pad_token_id=tokenizer.eos_token_id)
        result = text + tokenizer.decode(generated_ids[0], skip_special_tokens=False)[len(text):]
        return result

    def predict2(self, text, pattern):
        tokenizer = AutoTokenizer.from_pretrained(self.model, load_in_4bit=True)
        model = AutoModelForCausalLM.from_pretrained(self.model, trust_remote_code=True, revision="main")
        inputs = tokenizer(text, return_tensors="pt")
        sample = model.generate(**inputs, max_length=128, pad_token_id=tokenizer.eos_token_id)
        result = tokenizer.decode(sample[0], truncate_before_pattern=pattern)
        return result

    def answer(self, question, context):
        tokenizer = AutoTokenizer.from_pretrained(self.model, load_in_4bit=True)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.model)
        input = f"question: {question} context: {context}"
        encoded_input = tokenizer([input],
                                  return_tensors='pt',
                                  truncation=True)
        output = model.generate(input_ids=encoded_input.input_ids,
                                attention_mask=encoded_input.attention_mask,
                                max_new_tokens=128)
        output = tokenizer.decode(output[0], skip_special_tokens=True)
        return output

    @staticmethod
    def __get_model(model_type: str):
        """ Получение модели по типу. """
        return {
            'Codegen2_1': 'Salesforce/codegen2-1B',
            'Codegen2_3': 'Salesforce/codegen2-3_7B',
            'Codegen2_16': 'Salesforce/codegen2-16B',
            'Codet5p_2': 'Salesforce/codet5p-2b',
            'Starcoder': 'bigcode/starcoder',
            'facebook_125': 'facebook/opt-125m',
            't5_base': 'MaRiOrOsSi/t5-base-finetuned-question-answering',
        }.get(model_type)
