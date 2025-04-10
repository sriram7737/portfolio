from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

from peft import PeftModel
from transformers import AutoModelForCausalLM

base_model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = PeftModel.from_pretrained(base_model, "sriram7737/resume")

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1
)

def tailor_resume(job_description):
    prompt = f"""
    Given the job description below, generate a tailored resume snippet that matches the role:

    Job Description:
    {job_description}

    Tailored Resume:
    """
    result = generator(prompt, max_new_tokens=300, do_sample=True, temperature=0.7)[0]['generated_text']
    return result.split("Tailored Resume:")[-1].strip()
