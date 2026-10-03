# ai-productivity-toolkit
## Day 6: Zero-shot vs Few-shot Prompting
Zero-shot (no examples): "Classify the sentiment: 'The food was cold and the service was slow.'" → negative
Few-shot (3 examples given first, same text): → Negative
Both gave the same correct answer here because sentiment is a simple task. Few-shot helps more on harder or more specific tasks, since it shows the model the exact format and pattern to follow.
## Role + Context + Instruction + Constraint Prompt
Prompt: acted as a teacher, explaining to a 10-year-old, with the instruction to explain seasons in under 40 words.
Output: "Earth has seasons." (just repeated the question, did not actually explain)

Learning: A well-structured prompt (role, context, instruction, constraint) helps, but a small model like flan-t5-base can still fail on multi-part instructions. Prompt engineering improves results, but it can't fully fix a model that's too weak for the task. Larger models like GPT-4 or Claude handle layered instructions much better.
