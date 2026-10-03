# ai-productivity-toolkit
## Day 6: Zero-shot vs Few-shot Prompting
Zero-shot (no examples): "Classify the sentiment: 'The food was cold and the service was slow.'" → negative
Few-shot (3 examples given first, same text): → Negative
Both gave the same correct answer here because sentiment is a simple task. Few-shot helps more on harder or more specific tasks, since it shows the model the exact format and pattern to follow.
## Role + Context + Instruction + Constraint Prompt
Prompt: acted as a teacher, explaining to a 10-year-old, with the instruction to explain seasons in under 40 words.
Output: "Earth has seasons." (just repeated the question, did not actually explain)

Learning: A well-structured prompt (role, context, instruction, constraint) helps, but a small model like flan-t5-base can still fail on multi-part instructions. Prompt engineering improves results, but it can't fully fix a model that's too weak for the task. Larger models like GPT-4 or Claude handle layered instructions much better.
## Day 7: Structured Outputs, Summarization, Classification
- Asked the model to extract name/age as JSON from a sentence.
- Asked it to summarize a paragraph about GenAI in one sentence.
- Asked it to classify an email as Spam or Not Spam.
Learning: Giving an exact output format (like a JSON template) in the prompt makes the model's output far easier to use in real code, instead of free-form text.
## Day 8: AI-Assisted Coding and Debugging
- Asked the model to write a function to check if a number is prime.
- Asked it to find the bug in a faulty add() function (it uses - instead of +).
Learning: AI can draft code and spot simple bugs fast, but small models often give incomplete or wrong code, so always test the output yourself. Tools like GitHub Copilot or Claude Code do this far better than flan-t5-base.
## Day 9: Reusable Templates and Testing
Built 2 reusable prompt functions: summarize() and classify(). Ran 3 test cases through them.

| Input                                     | Function    | Output           |
|-------------------------------------------|-------------|------------------|
| "I love this product, it works great!"    | classify    | Positive         |
| "This is the worst purchase I ever made." | classify    | Negative         |
| "AI is a branch of computer science..."   | summarize   | (your output)    |

Learning: Wrapping prompts in functions makes them reusable across different inputs, which is the first step toward building a real AI tool instead of one-off prompts.
## Day 10: AI Productivity Toolkit
Built toolkit.py with 5 reusable functions:
- summarize(text)
- classify(text)
- write_email(topic)
- improve_resume_line(line)
- explain_code(code)

This toolkit wraps common prompt patterns (summarization, classification, email drafting, resume help, code explanation) into reusable functions, so they can be reused across any project.
