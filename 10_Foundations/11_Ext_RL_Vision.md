# 扩展：强化学习

层：扩展。当前阶段不读。主动视点或 Paper 6 再打开。

参考：Sutton, Barto. *Reinforcement Learning: An Introduction*. 2nd ed. http://incompleteideas.net/book/the-book-2nd.html

## 必学

状态 $s$，动作 $a$，奖励 $r$。策略 $\pi(a\mid s)$ 是在 $s$ 选 $a$ 的概率。折扣 $\gamma\in[0,1)$。回报

$$
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
$$

$t$ 是时间步。$\gamma$ 接近 1 更看远期。

状态值 $V^\pi(s)=\mathbb{E}[G_t\mid s_t=s]$。动作值 $Q^\pi(s,a)$ 是先做 $a$ 再按 $\pi$ 走的期望回报。策略梯度更新的是 $\pi$ 的参数；Q 学习更新的是 $Q$。

## 查阅

PPO、DQN 的目标网络、多智能体：知道是稳定训练或多人同时决策的做法。主动视点把下一相机位姿当成 $a$，奖励来自信息增益减飞行代价。
