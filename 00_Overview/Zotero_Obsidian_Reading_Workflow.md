# Zotero × Obsidian 阅读流程

版本：Obsidian 1.13.7，Zotero 桌面版（菜单按「编辑 → 设置」）。  
插件：Zotero 端 Better BibTeX；Obsidian 端 **Zotero Integration**（已装 `obsidian-zotero-desktop-connector`）。

Zotero 管「这篇放哪一类、读到哪、PDF 和划线」。  
Obsidian 管「精读判断」。  
两边收藏集**不对齐**仓库文件夹。导入时再选输出目录。

PDF 不进 Git（`*.pdf` 已忽略）。不要勾选 Copy attachments into vault。

---

## 1. Zotero 收藏集（建这一棵即可）

在「我的文库」下新建，名称按下面逐字建。一篇条目只放**一个**课题子夹；第二课题用「相关」拖关联，不要复制附件。

```text
00_收件箱_Inbox
01_正在读_Reading
P0_EI_航拍时延小目标
    P0_01_基线_Baseline
    P0_02_方法与协议_Method
    P0_03_近邻对照_Neighbor
    P0_04_评价口径_Eval
    P0_05_可引结论_Cite
    P0_06_不采用_Skip
A_RailUAV_SOD_铁路航拍数据文
    A_01_基线_Baseline
    A_02_方法与协议_Method
    A_03_近邻对照_Neighbor
    A_04_评价与数据规范_Eval
    A_05_可引结论_Cite
    A_06_不采用_Skip
B_Paper1_开放世界告警
    B_01_基线_Baseline
    B_02_方法_Method
    B_03_近邻对照_Neighbor
    B_04_评价口径_Eval
    B_05_可引结论_Cite
    B_06_不采用_Skip
P2_三维灾害量化
    P2_01_基线_Baseline
    P2_02_方法_Method
    P2_03_近邻对照_Neighbor
    P2_05_可引结论_Cite
P3_通信与风险共享
    P3_01_基线_Baseline
    P3_02_方法_Method
    P3_03_近邻对照_Neighbor
    P3_05_可引结论_Cite
P4_通感资源分配
    P4_01_基线_Baseline
    P4_02_方法_Method
    P4_03_近邻对照_Neighbor
    P4_05_可引结论_Cite
P5_多模态风险
    P5_01_基线_Baseline
    P5_02_方法_Method
    P5_03_近邻对照_Neighbor
    P5_05_可引结论_Cite
P6_主动复检
    P6_01_基线_Baseline
    P6_02_方法_Method
    P6_03_近邻对照_Neighbor
    P6_05_可引结论_Cite
P7_多机联合决策
    P7_01_基线_Baseline
    P7_02_方法_Method
    P7_03_近邻对照_Neighbor
    P7_05_可引结论_Cite
90_人物与期刊追踪_Watch
99_全局不采用_Skip
```

未开题的 P2–P7 可以先只建父夹，子夹等开题再建。当前只往 `P0_*` 里堆精读。

### 子夹放什么

| 子夹                   | 放                                      | 不放                            |
| -------------------- | -------------------------------------- | ----------------------------- |
| `*_01_基线_Baseline`   | 我方必须比对的笨方法：整图加大、均匀切、经典检测器、经典信道/优化器、不融合 | 作者自己的新模块                      |
| `*_02_方法与协议_Method`  | 机制或推理/传输/分配流程本身，用来学做法                  | 只报数、无机制的评测文                   |
| `*_03_近邻对照_Neighbor` | 和我方主张容易撞车的工作                           | 纯背景综述                         |
| `*_04_评价口径_Eval`     | 指标定义、划分、官方工具、硬件计时怎么报                   | 方法创新主文（那种进 02）                |
| `*_05_可引结论_Cite`     | 已经决定 Related Work / 正文会引用的数字或边界句       | 还没读完的                         |
| `*_06_不采用_Skip`      | 该课题下已判定无关或与冻结主张冲突                      | 以后可能开题再用的（那种留父夹 + `prio/ref`） |
|                      |                                        |                               |

`00_收件箱_Inbox`：刚下、还没定课题。每周清空。  
`01_正在读_Reading`：本周正在划线的，读完必须拖走。  
`90_人物与期刊追踪_Watch`：只盯作者/会刊，不精读。  
`99_全局不采用_Skip`：与整条博士线都无关。

同一篇既是近邻又会被引用：主放 `03_近邻`，读完决定引用后再**移动**到 `05_可引结论`，不要两份 PDF。

---

## 2. 标签（含义固定，不要自造近义词）

在条目上打标签，可多选。收藏集=位置，标签=状态和角色。

### 状态（每篇恰好一个）

| 标签 | 含义 | 何时打 |
|---|---|---|
| `status/toread` | 入库未读 | 拖进 Inbox 时 |
| `status/reading` | 正在划线 | 打开 PDF 时；同时放入 `01_正在读_Reading` |
| `status/read` | PDF 读完且至少有一条高亮或批注 | 关 PDF 前；此时才允许导入 Obsidian |
| `status/noted` | Obsidian 精读各节已手填，不是空模板 | 填完精读笔记后 |
| `status/cited` | 数字或一句结论已进矩阵或大纲 | 写回矩阵后 |
| `status/skip` | 不再读、不导入 | 进任何 `*_Skip` 时 |

改状态时去掉旧状态标签，只留当前这一个。

### 路线（一篇可多个，但必须有一个主路线）

| 标签 | 含义 |
|---|---|
| `route/p0` | 练手 EI |
| `route/a` | RailUAV-SOD 数据文 |
| `route/b` | Paper 1 |
| `route/p2` … `route/p7` | 对应正式论文 |
| `route/watch` | 只追踪，不进主张 |

### 角色（可多选，须与子夹一致）

| 标签 | 含义 |
|---|---|
| `role/baseline` | 我方实验必须出现的对照 |
| `role/method` | 要搞懂的机制或协议 |
| `role/neighbor` | 可能部分覆盖我方问题 |
| `role/eval` | 只贡献怎么评、怎么划分、怎么计时 |
| `role/dataset` | 数据发布或标注规范 |
| `role/survey` | 综述 |
| `role/negative` | 用来卡边界的反例（他们做了我们明确不做的） |

### 优先级（每篇恰好一个）

| 标签 | 含义 |
|---|---|
| `prio/must` | 现在必须精读，可导入 Obsidian |
| `prio/rec` | 开题或写 Related Work 再精读 |
| `prio/ref` | 只留条目，默认不导入 |

当前阶段：只有 `route/p0` + `prio/must` + `status/read` 才导入精读笔记。

---

## 3. 第一次配置（做完不用再做）

### 3.1 Zotero

1. 打开 Zotero。`工具 → 插件`，安装 Better BibTeX 的 `.xpi`，重启。  
2. `编辑 → 设置 → Better BibTeX`，Citation key 公式保持 `auth.lower + shorttitle(3,3) + year`。不要打开 “Regenerate citation key when item changes”。  
3. 文库里已有条目：全选该库 → 右键 → `Better BibTeX → Refresh citation keys`（只做一次）。  
4. `编辑 → 设置 → 高级`：勾选 **允许其他应用程序与 Zotero 通信**。  
5. 按第 1 节建收藏集。  
6. PDF 一律用 Zotero 内置阅读器（双击附件）。不要只在外部阅读器划线。

### 3.2 Obsidian

1. 打开本仓库 Vault。设置 → 第三方插件 → **Zotero Integration** 为开。  
2. 设置 → Zotero Integration → Database 选本机正在运行的 Zotero。  
3. 建导入格式，名称必须与下面命令里用的一致：

| Import Format 名称 | Output path |
|---|---|
| `P0-CloseRead` | `00_Practice_UAV_Aerial_Detection/Literature/notes/{{citekey}}.md` |
| `A-CloseRead` | `08_RailUAV_SOD/Literature/notes/{{citekey}}.md` |
| `B-CloseRead` | `01_Paper1_OpenWorld_Risk/Literature/notes/{{citekey}}.md` |
| `P2-CloseRead` | `02_Paper2_3D_Disaster/Literature/notes/{{citekey}}.md` |
| （P3–P7 同理） | `0n_.../Literature/notes/{{citekey}}.md` |

每条格式：

- Template file：`00_Overview/Zotero_Import_Template.md`（见第 6 节；若文件尚无，把第 6 节全文存成该路径）
- Copy attachments into vault：**关闭**
- 导入批注：**打开**
- Image output path：`99_Attachments/Zotero_Annot/{{citekey}}/`

4. 命令面板运行一次 `Zotero Integration: Data Explorer`，选一篇有 PDF 的条目，确认能看到 title、citekey、annotations。看不到则回到 3.1 第 4 步。
5. 执行 `Zotero Integration: Create literature note from selected item(s)`，可以生成笔记

---

## 4. 日常：从下到读完到笔记（逐步操作）

下列每一步都写清在哪个软件点什么。当前只对 P0 走到第 4.8；A/B、P2–P7 停在 4.3，打 `prio/ref` 即可。

### 4.1 入库（Zotero）

1. 用 Zotero Connector 或「通过标识符添加」写入条目。  
2. 确认有 PDF 附件。没有则「添加附件 → 存储副本」或链接本地文件。  
3. 把条目拖到 `00_收件箱_Inbox`。  
4. 标签：`status/toread`。此时不要打路线。

### 4.2 定课题与角色（Zotero）

1. 读标题和摘要（条目右窗即可，不必开 PDF）。  
2. 从 Inbox **拖到**对应课题的某一个子夹（基线 / 方法 / 近邻 / 评价 / 不采用）。  
3. 去掉 Inbox 位置（拖走即离开 Inbox）。  
4. 打一个 `route/*`、一个 `prio/*`、需要的 `role/*`。  
5. 若判定无关：拖到该课题 `*_06_不采用_Skip` 或 `99_全局不采用_Skip`，状态改成 `status/skip`，**不要**做 4.4 之后的导入。

### 4.3 开始读（Zotero）

1. 条目再拖一份到 `01_正在读_Reading`（Zotero 允许同一条目出现在多个收藏集；读完在 4.5 里从「正在读」移除）。  
2. 标签：删 `status/toread`，打 `status/reading`。  
3. 双击 PDF，在 **Zotero 阅读器**里划线。  
4. 自己的判断写在批注框（选中高亮 → 添加注释），不要只涂色。页码会随批注进 Obsidian。

### 4.4 读完（Zotero）

1. 关闭 PDF（先确认划线已保存，标题栏无未保存提示）。  
2. 标签：删 `status/reading`，打 `status/read`。  
3. 在 `01_正在读_Reading` 上右键该条目 → 从收藏集中移除（条目仍留在课题子夹）。  
4. 打开条目，看右侧 Citation Key 是否稳定，记下这个 key（将是 md 文件名）。

### 4.5 导入笔记（Obsidian + Zotero 都开着）

1. Zotero：单击该条目，保持选中。  
2. 切到 Obsidian。`Ctrl+P`（macOS `Cmd+P`）→ `Zotero Integration: Create literature note from selected item(s)`。  
3. 选 Import Format：P0 用 `P0-CloseRead`，不要选错成 A/B。  
4. 等待新标签页打开 `Literature/notes/{{citekey}}.md`。  
5. 检查文末「划线与批注」是否有刚画的线。没有则回到 Zotero 用内置阅读器补一条高亮，再执行本小节第 2–3 步（有 persist 时不会冲掉已写正文）。

### 4.6 填精读（Obsidian）

1. 只手填模板里仍空的节：问题、机制、数据、实验数字、主张、对应关系。  
2. 数字必须能指回原文表号或节。  
3. 「对应关系」里写主挂靠、冲突、下一步。  
4. 保存文件（Obsidian 默认自动保存则切换窗口即可）。

### 4.7 标记已做笔记（Zotero）

1. 回到 Zotero 该条目。  
2. 删 `status/read`，打 `status/noted`。  
3. 不要移动收藏集，除非已决定引用（见 4.8）。

### 4.8 写回矩阵并决定是否引用（Obsidian，然后 Zotero）

1. Obsidian：打开该方向 `Literature/Literature_Matrix.md`，找到或新增一行，写入一行结论（用笔记里的「一句结论」）。  
2. 若这篇确定进 Related Work / 正文：Zotero 中把条目**从** `03_近邻` 或 `02_方法` **拖到** `05_可引结论_Cite`，标签加 `status/cited`（可与 `status/noted` 并存；cited 表示已落地写作，noted 表示笔记写完——若只保留一个状态，改用 `status/cited` 并保证笔记已存在）。  
3. 若决定不用：拖到 `*_06_不采用_Skip`，状态改为 `status/skip`。Obsidian 笔记保留，文件名不要删，避免下次重复导入。

### 4.9 补划线（已导入之后）

1. Zotero 再打开同一 PDF，追加高亮。  
2. Obsidian 再跑 4.5 第 2–3 步，同一 Format、同一条目。  
3. 只应更新文末批注块。若上半精读被清空，停止导入，检查模板是否含 `{% persist "annotations" %}`。

---

## 5. 每周一次（Zotero）

1. 点开 `00_收件箱_Inbox`：留下的条目必须在当周完成 4.2，否则标 `status/skip` 进 `99_全局不采用_Skip`。  
2. 点开 `01_正在读_Reading`：超过 7 天仍在此的，要么当天做完 4.4，要么移出并改回 `status/toread`。  
3. 不要对 `prio/ref`、`status/skip`、Watch 集合执行导入命令。

---

## 6. 导入模板正文

将下面存为 `00_Overview/Zotero_Import_Template.md`，并在各 Import Format 的 Template file 中指向它。

```text
# 精读笔记：{{citekey}}

## 题目

{{title}}

## 作者 / 年 / Venue

{% for c in creators %}{{c.lastName}}{% if not loop.last %}, {% endif %}{% endfor %} / {{date | format("YYYY")}} / {{publicationTitle or proceedingsTitle or university}}

## DOI 或 arXiv

{% if DOI %}https://doi.org/{{DOI}}{% endif %}

## Zotero

[打开条目]({{desktopURI}})

## 为什么读


## 问题


## 机制

输入 → 做什么 → 输出：

相对最笨做法多了哪一步：

## 数据

集合与划分：

标注 / 忽略规则：

预训练与泄漏：

## 实验

主表在比什么：

关键数字（方法，集合，指标，数值，表号）：

-

强简单基线：

消融或失败：

计时 / 硬件口径：

## 主张

1.
2.

作者承认的局限：

稿子暗示但没做的：

证据撑不撑主张：

## 可抄结构

章节顺序：

主表列名：

方法图块名：

## 对应关系

### 问题类型

### 主挂靠

### 次挂靠

### 关系

### 新颖性冲突

### 冲突理由

### 对已冻结主张的影响

### 是否改边界

### 下一步

## 一句结论

## 未解决

{% persist "annotations" %}
## 划线与批注

{% for a in annotations %}
- p.{{a.pageLabel}} {{a.annotatedText}}
  {% if a.comment %}注：{{a.comment}}{% endif %}
{% endfor %}
{% endpersist %}
```

精读手写规范仍以 [Paper_Close_Reading_Template.md](Paper_Close_Reading_Template.md) 为准；导入模板与它同节，避免两套结构。

---

## 7. 对不上号

| 现象 | 处理 |
|---|---|
| Obsidian 报连不上 Zotero | 先开 Zotero，再查「允许其他应用程序通信」 |
| 有笔记无划线 | 线画在外部阅读器；用内置阅读器重画一条再导入 |
| 文件出现在错误 `Literature/notes` | 选错 Import Format；把 md 移到正确目录，Zotero 侧不要复制条目 |
| 二次导入清空手写 | 模板缺 persist；补第 6 节后再导 |
| citekey 变了 | 关闭 BBT 自动重生；旧 md 改名与新 key 一致 |
| 同一 PDF 两份笔记 | 只留 `{{citekey}}.md`；删掉「副本」「(1)」 |
