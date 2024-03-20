from llm_usage import infer_with_template
import requests
import json
import time

max_response_time = 3

def send_request(endpoint):
    response = requests.get(endpoint)
    return response

def test_responsetime():
    TEMPLATE = """<s>[INST] <<SYS>>
Answer below truthfully and in less than 10 words:
<</SYS>>
{silly_question}
[/INST]"""
    
    start = time.perf_counter()
    response = infer_with_template("Who saw a saw saw a salsa?", TEMPLATE)
    response_time = time.perf_counter() - start

    if response_time>max_response_time:
        raise Exception(f"Response took {response_time} which is greater than {max_response_time}")

    print(f"Response time was OK at {response_time} seconds")

    with open("responsetime_result.json", "w") as f:
        json.dump({
            "response_time": response_time
        }, f)

if __name__ == '__main__':
    test_responsetime()