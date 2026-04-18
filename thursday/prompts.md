# AI Prompts Documentation

In accordance with the assignment's AI Usage Policy, here are the AI prompts utilized during the creation of this project.

## Sub-step 1 & 3: LSTM Sequence Modeling
**Prompt:** "Write a clean PyTorch implementation for Next-day Close Stock Prediction using `Day 47 stock_prices.csv`. Requirements: function to generate sequence dataset natively, chronologic splitting without data leakage, simple 1-layer LSTM using torch.nn.LSTM, RMSE error calculation on test."

**Critique:** The initial model did not automatically denormalize the dataset back before returning predictions, which creates misleading RMSE. I manually adjusted the code to `close_min, close_max` variables and applied denormalization back into actual numbers at the evaluation block before calculating RMSE. 

## Sub-step 6: Autoregressive Baseline
**Prompt:** "Using the same sequences generated above, build a linear regression Autoregressive (AR) model using sklearn's LinearRegression to serve as a baseline to the LSTM. Plot the comparison."

**Critique:** AI output was correct and effectively flattened the sliding window into vector representations for LinearRegression to handle.

## Sub-step 7: Manual BPTT 
**Prompt:** "Provide a manual implementation of Backpropagation Through Time (BPTT) for a single layer RNN in numpy without autograd to show the Vanishing Gradient problem on sequences length 5 vs 50. Output exactly the gradients and standard norm magnitudes to graph."

**Critique:** AI correctly handled the derivative of `tanh`. I added an evaluation section at the end to automatically plot the resulting gradients to show exponential decay explicitly, fulfilling the documentation requirements heavily emphasized in the assignment.
