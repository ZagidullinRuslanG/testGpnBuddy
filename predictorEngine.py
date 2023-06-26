from transformers import AutoModelForCausalLM, AutoTokenizer
from enum import Enum


class PredictorEngine:

    def __init__(self):
        self.model = Model.Codegen2_1
        self.device = "cpu"

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.model)
        model = AutoModelForCausalLM.from_pretrained(self.model, trust_remote_code=True, revision="main").to(self.device)

        input_ids = tokenizer(text, return_tensors="pt").input_ids
        generated_ids = model.generate(input_ids, max_length=128, pad_token_id=tokenizer.eos_token_id)
        result = text + tokenizer.decode(generated_ids[0], skip_special_tokens=False)[len(text):]
        return result


class Model(Enum):
    Codegen2_1 = "Salesforce/codegen2-1B"
    Codegen2_3 = "Salesforce/codegen2-3_7B"
    Codegen2_16 = "Salesforce/codegen2-16B"
    Codet5p_2 = "Salesforce/codet5p-2b"
    Starcoder = "bigcode/starcoder"
