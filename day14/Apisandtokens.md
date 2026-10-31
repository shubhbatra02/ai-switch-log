Tokens are small pieces of text that a language model can read or write.Text is first cut into tokens, and everything the model does, including its cost and its limits, is counted in them.

A token is often a whole short word, part of a longer word, a punctuation mark, or a space plus a word. For example, “unbelievable” might become un + believ + able, and “ORA-01555” could split into several pieces. In English, a rough rule is 1 token is about 4 characters, or about three-quarters of a word, so 100 words is roughly 130 tokens. That’s only an estimate, and every model has its own tokenizer.

Why they matter

Cost. APIs charge per token, with separate rates for input (your prompt plus any documents you include) and output (what the model writes). Output usually costs more per token.
The context window. Each model has a maximum number of tokens it can handle in one request, covering your prompt, the conversation history and the reply together. If you go over it, the request fails or old text is dropped. This is the real reason RAG exists: you can’t paste a whole documentation library into the prompt, so you retrieve only the few relevant chunks.
Limits and speed. Rate limits are often counted in tokens per minute, and longer outputs take longer to generate.
Control. APIs have a setting for the maximum output length, which caps both cost and rambling replies.

the context window is the model’s working memory for one request, and everything you send plus everything it writes has to fit in it.