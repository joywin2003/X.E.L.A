response = {"choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "hi there"
      },
      "finish_reason": "length"
    }
  ]}
print(response.choices.content)
