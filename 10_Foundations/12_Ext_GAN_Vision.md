# 扩展：GAN

层：扩展。当前阶段不读。

参考：Goodfellow et al. Generative Adversarial Nets. NeurIPS 2014. https://papers.nips.cc/paper/5423-generative-adversarial-nets

## 必学

生成器 \(G\) 把噪声 \(z\) 变成样本 \(G(z)\)。\(z\) 常取标准正态。判别器 \(D(x)\) 输出 \(x\) 像真样本的分数，范围 \((0,1)\)。

\[
\min_G\max_D\ \mathbb{E}_{x\sim p_{\mathrm{data}}}[\log D(x)]+\mathbb{E}_{z}[\log(1-D(G(z)))]
\]

\(p_{\mathrm{data}}\) 是真数据分布。第一项让 \(D\) 认出真样本，第二项让 \(G\) 骗过 \(D\)。

## 查阅

WGAN 改距离，减轻模式崩塌。条件 GAN 加类别或文本。扩散模型是另一步步去噪，不是这一式的特例。
