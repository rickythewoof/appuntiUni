The `(1 - self.lr)` term comes from rearranging the standard Q-learning update rule into a linear interpolation form.

The standard update rule is: $Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$

Let's substitute $\alpha$$\alpha$ with `self.lr` and define the target $T = r + \gamma \max_{a'} Q(s', a')$$T = r + \gamma \max_{a'} Q(s', a')$. The update becomes: $Q(s, a) \leftarrow Q(s, a) + \text{self.lr} [T - Q(s, a)]$$Q(s, a) \leftarrow Q(s, a) + \text{self.lr} [T - Q(s, a)]$

Now, let's expand and rearrange this equation: $Q(s, a) \leftarrow Q(s, a) + \text{self.lr} \cdot T - \text{self.lr} \cdot Q(s, a)$$Q(s, a) \leftarrow Q(s, a) + \text{self.lr} \cdot T - \text{self.lr} \cdot Q(s, a)$ $Q(s, a) \leftarrow Q(s, a) - \text{self.lr} \cdot Q(s, a) + \text{self.lr} \cdot T$$Q(s, a) \leftarrow Q(s, a) - \text{self.lr} \cdot Q(s, a) + \text{self.lr} \cdot T$ $Q(s, a) \leftarrow (1 - \text{self.lr}) Q(s, a) + \text{self.lr} \cdot T$$Q(s, a) \leftarrow (1 - \text{self.lr}) Q(s, a) + \text{self.lr} \cdot T$

This last form is the linear interpolation form used in your code: `self.q_values[state][action] = (1 - self.lr) * old_q_value + self.lr * target`

where `old_q_value` is the current $Q(s, a)$$Q(s, a)$ and `target` is the $T = r + \gamma \max_{a'} Q(s', a')$$T = r + \gamma \max_{a'} Q(s', a')$.

So, the `(1 - self.lr) * old_q_value` term represents keeping a portion of the old Q-value, and the `self.lr * target` term represents adding a portion of the new target value. The learning rate `self.lr` determines how much weight is given to the new target value compared to the old Q-value. A higher learning rate means the agent learns more quickly from the new experience, while a lower learning rate means it relies more on its existing Q-value.

This linear interpolation form is mathematically equivalent to the standard update rule and is often used in implementations for its clarity in showing how the new Q-value is a weighted average of the old Q-value and the target value.

However, as I mentioned before, the calculation of `target` in your current code snippet is using `self.lr` instead of a discount factor `gamma`, which is not standard Q-learning.