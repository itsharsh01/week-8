# AI Documentation & Critiques

## Transfer Learning Implementation
**Prompt:** "Create a PyTorch `DataLoader` component and a Transfer Learning setup for ResNet18 that freezes the backbone correctly. Since I only have `medical_imaging_meta.csv` metadata, let the `__getitem__` function construct a deterministic random `np.uint8` array based on a hash of the image ID so we can effectively prototype."

**Critique:** The AI setup logic was correct for freezing `param.requires_grad = False` across the `resnet.parameters()`, effectively preserving the edge detectors initially learned on ImageNet while restricting training solely to the new linear top head. I modified the generated code to use `hash() % (2**32-1)` ensuring deterministic procedural image generation to fulfill the TA's evaluation constraints.

## Fine-Tuning Strategy
**Prompt:** "Extend this baseline feature extractor by unfreezing 'layer4'. Setup the new model function."

**Critique:** The AI simply tried to re-import a brand new model. I rewrote the segment to loop across `named_parameters()` of the *existing* model to explicitly unfreeze substrings matching `layer4` and unfreeze `fc`. This simulates true multi-staged domain adaptation where the tail layers morph to clinical data.

## Major Exam 1 Simulation
**Prompt:** "Generate a brief 200 word synthesis explaining Matrix Backpropagation for a classmate, and 2 mock interview questions/answers."

**Critique:** Output was overly technical at first. I condensed the explanation utilizing a 'water pipe' analogy to simplify how gradient routing occurs in linear layers and specifically tailored Q2 towards ReLU boolean masks since it is frequently queried in AI engineering interviews.
